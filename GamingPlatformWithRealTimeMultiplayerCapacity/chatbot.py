import json
import requests
import time
import urllib
from pprint import pprint
import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid

from tornado.options import define, options

TOKEN = '818565983:AAEVGo0gQ2yugr1MPhwVDz3LNTja19NSU7k'
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
text_question1 = 'http://c568adc5.ngrok.io/sentence'
face_detection = 'http://ef6cb556.ngrok.io'
image_captioning = 'http://54094669.ngrok.io'

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def fn_text(in_text):
    print(in_text)
    a= requests.post(url = text_question1, data = {"sentence":in_text})
    print(a)
    result = json.loads(a.text)
    question = result['success']['data']['question'][0]
    answer = result['success']['data']['answer'][0]
    return question, answer

def fn_face(in_text):
    print(in_text)
    a= requests.post(url = face_detection, data = {"url":in_text})
    print(a)
    result = json.loads(a.text)
    if 'success' in result:
        p_details = result['success']['data']['Person_details']
        g1 = result['success']['data']['Sports_Guess_1']
        g2 = result['success']['data']['Sports_Guess_2']
        g3 = result['success']['data']['Sports_Guess_3']
    else:
        p_details = {'error':2}
        g1 = 'result'
        g2 = 'result'
        g3 ='result'
    print(p_details, g1, g2, g3)
    return p_details, g1, g2, g3

def fn_image(in_text):
    print(in_text)
    a= requests.post(url = image_captioning, data = {"url":in_text})
    print(a)
    
    result = json.loads(a.text)
    if 'success' in result:
        d = result['success']['data']
    else:
        d = {'error':2}
    return d

def echo_all(updates):
    for update in updates["result"]:
        pprint(update)
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        abc = text.split(' ') 
        if abc[0] == 'text':
            question, answer = fn_text(' '.join(abc[1:]))
            print(question)
            print(answer)
            send_message(question, chat)
            send_message(answer, chat)
            # send_msg = '1' 
        elif abc[0] == 'face':
            p1, p2, p3, p4 = fn_face(' '.join(abc[1:]))
            # print('This is data')
            print(p1)
            send_message(json.dumps(p1), chat)
            send_message('------------Sports guesses-------------', chat)
            send_message(p2, chat)
            send_message(p3, chat)
            send_message(p4, chat)
        elif abc[0] == 'image':
            print(' '.join(abc[1:]))
            caption = fn_image(' '.join(abc[1:]))
            
            send_message(caption, chat)
            question, answer = fn_text(caption)
            # print(question)
            # print(answer)
            send_message(question, chat)
            send_message(answer, chat)
        else:
            send_message('Invalid Input', chat)
        
        # send_message(send_msg, chat)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()