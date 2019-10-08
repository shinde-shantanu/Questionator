from spcyques import create_questions
from gensim.summarization.summarizer import summarize
import json
import pandas as pd
import os
import spacy
from spacy import displacy
import nltk

nlp = spacy.load('en_core_web_sm')

obj={}

df=pd.read_csv("summary.csv")

for x in range(0,len(df.num)):
    try:
        a=df.summary[x]
        print(df.num[x])
        obj={}
        obj["sentence"]=a
        obj["features"],obj["question"],obj["answer"]=create_questions(a)
        with open("data2.json", "a") as outfile:
            json.dump(obj,outfile,indent=4)
    except Exception as e:
        print(e)
        pass
