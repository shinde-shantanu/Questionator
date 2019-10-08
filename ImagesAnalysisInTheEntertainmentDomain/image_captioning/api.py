# This is the final production api for the questionator api. Please run this if there is any plan of implementing the website.


import tornado.ioloop
import tornado.web
from sample import load_image
import urllib
import os
import torch
import matplotlib.pyplot as plt
import numpy as np 
import argparse
import pickle 
import os
from torchvision import transforms 
from build_vocab import Vocabulary
from model import EncoderCNN, DecoderRNN
from PIL import Image
from os import rename, listdir
import pandas as pd
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

parser = argparse.ArgumentParser()
parser.add_argument('--encoder_path', type=str, default='models/encoder-2-1000.ckpt', help='path for trained encoder')
parser.add_argument('--decoder_path', type=str, default='models/decoder-2-1000.ckpt', help='path for trained decoder')
parser.add_argument('--vocab_path', type=str, default='data/vocab.pkl', help='path for vocabulary wrapper')
	
# Model parameters (should be same as paramters in train.py)
parser.add_argument('--embed_size', type=int , default=256, help='dimension of word embedding vectors')
parser.add_argument('--hidden_size', type=int , default=512, help='dimension of lstm hidden states')
parser.add_argument('--num_layers', type=int , default=1, help='number of layers in lstm')
args = parser.parse_args()

prediction = []
transform = transforms.Compose([
	transforms.ToTensor(), 
	transforms.Normalize((0.485, 0.456, 0.406), 
						 (0.229, 0.224, 0.225))])
	
	# Load vocabulary wrapper
with open(args.vocab_path, 'rb') as f:
	vocab = pickle.load(f)

	# Build models
encoder = EncoderCNN(args.embed_size).eval()  # eval mode (batchnorm uses moving mean/variance)
decoder = DecoderRNN(args.embed_size, args.hidden_size, len(vocab), args.num_layers)
encoder = encoder.to(device)
decoder = decoder.to(device)

	# Load the trained model parameters
encoder.load_state_dict(torch.load(args.encoder_path))
decoder.load_state_dict(torch.load(args.decoder_path))

def getCaption(url):

	urllib.urlretrieve(url, os.getcwd()+'/'+str(1)+".jpg")

	image = load_image(os.getcwd()+'/'+str(1)+".jpg", transform)
	image_tensor = image.to(device)
		
	# Generate an caption from the image
	feature = encoder(image_tensor)

	sampled_ids = decoder.sample(feature)
	sampled_ids = sampled_ids[0].cpu().numpy()          # (1, max_seq_length) -> (max_seq_length)
		
	# Convert word_ids to words
	sampled_caption = []
	for word_id in sampled_ids:
		word = vocab.idx2word[word_id]
		
		if word == '<end>' or word=='<start>':
			pass	
		# if word == '<end>':
		else:
			sampled_caption.append(word)
	sentence = ' '.join(sampled_caption)
	


	return sentence

# This is the tornado api class. In order to hit it you need to POST request with the argument key 'url' which contains the url address of the  image for which caption needs to be generated.

class MainHandler(tornado.web.RequestHandler):
	def post(self):
		try:
			url=self.get_argument('url')
			print url

			op_o={}
			op_o["success"]={"code":"200","message":"successful","data":getCaption(url)}
			self.write(op_o)
		except Exception as e:
			op_o={}
			print e
			op_o["error"]={"code":"400","message":str(e)}
			self.write(op_o)

def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
	])

if __name__ == "__main__":
	app = make_app()
	app.listen(8880)
	tornado.ioloop.IOLoop.current().start()