import json                                              
import pandas as pd
import collections
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint
from sklearn.feature_extraction.text import CountVectorizer
import re
import csv
with open('data1.json') as f1:
    data=json.load(f1)
len(data['articles'])
art = data['articles']
df_idf = pd.DataFrame.from_dict(art)
df_idf['text'] = df_idf['description']
sentences = df_idf['text'].tolist()
def word_tokenizer(text):
    
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(t) for t in tokens if t not in stopwords.words('english')]
    return tokens
def cluster_sentences(sentences, nb_of_clusters=5):
    tfidf_vectorizer = TfidfVectorizer(tokenizer=word_tokenizer,
                                    stop_words=stopwords.words('english'),
                                    max_df=0.9,
                                    min_df=0.1,
                                    lowercase=True)
    
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    kmeans = KMeans(n_clusters=nb_of_clusters)
    kmeans.fit(tfidf_matrix)
    clusters = collections.defaultdict(list)
    for i, label in enumerate(kmeans.labels_):
            clusters[label].append(i)
    return dict(clusters)


nclusters= 5
clusters = cluster_sentences(sentences, nclusters)
for cluster in range(nclusters):
    print("cluster ",cluster,":")
    for i,sentence in enumerate(clusters[cluster]):
        print("\tsentence ",i,": ",sentences[sentence])


json_data = {} 
clust={}
for i in range(nclusters):
    if i not in json_data:
            print("cluster ",i,":")
            json_data[i]=[]
            
            for j,sentence in enumerate(clusters[i]):
                json_data[i].append(sentences[sentence])
                
           
print(json_data)