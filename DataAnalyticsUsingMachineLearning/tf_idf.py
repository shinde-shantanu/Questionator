import json
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

def pre_process(text):
    
    text=text.lower()
    text=re.sub("</?.*?>"," <> ",text)
    text=re.sub("(\\d|\\W)+"," ",text)
    return text
def get_stop_words(stop_file_path):
    """load stop words """
    
    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)
        return frozenset(stop_set)

def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    for idx, score in sorted_items:
        fname = feature_names[idx]
        
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    results= {}             
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results

def get_keywords(idx):

    tf_idf_vector=tfidf_transformer.transform(cv.transform([docs_test[idx]]))
    sorted_items=sort_coo(tf_idf_vector.tocoo())
    keywords=extract_topn_from_vector(feature_names,sorted_items,10)
    return keywords

def print_results(idx,keywords):
    # now print the results
    print("\nTitle")
    print(docs_title[idx])
    print("\nDescroption")
    print(docs_body[idx])
    print("\nKeywords")
    for k in keywords:
        print(k,keywords[k])



with open('data1.json') as f:
    data=json.load(f)

art = data['articles']
df_idf = pd.DataFrame.from_dict(art)
df_idf['text'] = df_idf['title']+df_idf['description']
df_idf['text'] = df_idf['text'].apply(lambda x:pre_process(x))
df_idf['text'][2]
stopwords=get_stop_words("resources/stopwords.txt")
docs=df_idf['text'].tolist()
cv=CountVectorizer(max_df=0.85,stop_words=stopwords)
word_count_vector=cv.fit_transform(docs)

tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)
print(cv.vocabulary_.keys())
print(tfidf_transformer.idf_)

with open('data.json') as f2:
    data1=json.load(f2)
art = data['articles']
df_test = pd.DataFrame.from_dict(art)


df_test['text'] = df_idf['title']+df_idf['description']
df_test['text'] =df_test['text'].apply(lambda x:pre_process(x))


docs_test=df_test['text'].tolist()
docs_title=df_test['title'].tolist()
docs_desc=df_test['description'].tolist()

feature_names=cv.get_feature_names()
doc=docs_test[0]
tf_idf_vector=tfidf_transformer.transform(cv.transform([doc]))

sorted_items=sort_coo(tf_idf_vector.tocoo())
keywords=extract_topn_from_vector(feature_names,sorted_items,10)

print("\nTitle")
print(docs_title[0])
print("\nDescription")
print(docs_desc[0])
print("\nKeywords")
for k in keywords:
    print(k,keywords[k])


idx=28
keywords=get_keywords(idx)
print_results(idx,keywords)