import spacy
from spacy import displacy
import nltk

def create_questions(ip):
    all_ques=[]
    all_ans=[]
    all_fet=[]
    
    nlp = spacy.load('en_core_web_sm')
    
    sent = nltk.tokenize.sent_tokenize(ip)
    for a in sent:

        ##Performing named entity recognition using Spacy-
        doc = nlp(a)
        ans=a

        ##Feature vector-
        features={"GPE":0,
            "MONEY":0,
            "ORG":0,
            "DATE":0,
            "PERSON":0,
            "EVENT":0,
            "LOC":0,
            "PRODUCT":0,
            "LANGUAGE":0,
            "TIME":0,
            "PERCENT":0,
            "QUANTITY":0,
            "WORK_OF_ART":0,
            "CARDINAL":0,
            "NNP":0,
            "CD":0,
            "NN":0,
            "NOUN":0,
            "NUM":0,
            "RB":0}
        
        ##Rules for question generation-
        ne={"GPE":"which location",
            "MONEY":"how much money",
            "ORG":"which organization",
            "DATE":"when",
            "PERSON":"who",
            "EVENT":"what",
            "LOC":"where",
            "PRODUCT":"what",
            "LANGUAGE":"which language",
            "TIME":"when",
            "PERCENT":"what percent",
            "QUANTITY":"how much",
            "WORK_OF_ART":"what",
            "CARDINAL":"how many"}
        pos={"NNP":"who",
             "CD":"how many",
             "NN":"what",
             "NOUN":"what",
             "NUM":"how many",
             "RB":"how"}
        #"ner-"
        for ent in doc.ents:
            if ent.label_ in ne:
                features[ent.label_] = features[ent.label_] + 1
                ans = ans[0:ent.start_char] + ne[ent.label_] + ans[ent.end_char:len(ans)] +"?"
                all_ques.append(ans)
                all_ans.append(str(ent))
                #all_fet[str(ent)]=ent.label_
                ans=a
        ans=""
        for p in pos:
            for i in range(0,len(doc)):
                if doc[i].tag_ == p:
                    features[p] = features[p] + 1
                    a1=ans
                    a1 += pos[p] + " "
                    answer=doc[i]
                    for j in range(i+1,len(doc)):
                        a1 += doc[j].text + " "
                    all_ques.append(a1)
                    all_ans.append(str(answer))
                    #all_fet[str(answer)]=p
                ans += doc[i].text + " "
            ans=""

        for x in features:
            all_fet.append(features[x])
        
        return all_fet,all_ques,all_ans

