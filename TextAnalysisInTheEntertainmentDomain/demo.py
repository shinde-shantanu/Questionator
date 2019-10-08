import spacy
from spacy import displacy
import nltk

nlp = spacy.load('en_core_web_sm')
ip = input("Enter the sentence: ")
sent = nltk.tokenize.sent_tokenize(ip)
for a in sent:
    doc = nlp(a)
    ans=a
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
    print("ner-")
    for ent in doc.ents:
        if ent.label_ in ne:
            ans = ans[0:ent.start_char] + ne[ent.label_] + ans[ent.end_char:len(ans)] +"?"
            print(ans)
            print(ent)
            ans=a
    ans=""
    print("pos-")
    for p in pos:
        for i in range(0,len(doc)):
            if doc[i].tag_ == p:
                a1=ans
                a1 += pos[p] + " "
                answer=doc[i]
                for j in range(i+1,len(doc)):
                    a1 += doc[j].text + " "
                print(a1)
                print(answer)
            ans += doc[i].text + " "
        ans=""
    
