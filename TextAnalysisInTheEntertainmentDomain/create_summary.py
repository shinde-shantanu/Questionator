import os
from gensim.summarization.summarizer import summarize
import pandas as pd

df = pd.DataFrame(columns=["num",
                           "summary"])


path="C:/Users/Shantanu Shinde/Desktop/Shantanu/Machine Learning/bbc/sport"
l = os.listdir(path)
for x in l:
    p=path
    p=path+"/"+x
    print(x)
    f=open(p,"r")
    ip=f.read()
    summ=summarize(ip,word_count=25)
    df2 = pd.DataFrame([[x,summ]],columns=["num",
                           "summary"])
    df=df.append(df2)

df.to_csv('summary.csv')
