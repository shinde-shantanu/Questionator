import spacy
import nltk
from nltk.parse.corenlp import CoreNLPDependencyParser
nlp=spacy.load("en_core_web_sm")
dep_parser=CoreNLPDependencyParser(url="http://localhost:9000")    
class Helper():
    def questionator(self,sentence):
        flag=0
        string1=""
        sentences=[]
        object1=""
        ans=""
        sub_type=""
        subject=""
        sentences.append(sentence)
        try:
            parse,=dep_parser.raw_parse(sentence)
        except:
            print('error')
            
        for sentence in sentences:
            #print(sentence)
                #print(parse.to_conll(4)) 
            for governer,dep,dependent in parse.triples():
                #print(dependent)
                #print(dep)
                #print(governer)
                if dep=='nsubjpass' or dep=='nsubj' or dep=='csubjpass' or dep=='xsubj':
                    
                    subject=dependent[0]
                    sub_type=dependent[1]
                    
                if dep=='nmod':
                    object1=dependent[0]
                if dep=='cc' or dep=='conj' or dep=='preconj':
                    #print('COMPLEX SENTENCE')
                    #flag=1
                    subject=" "
                    break
                
            #to check if there is a location kind question that can be generated
            if object1!="":
                loc_check = nlp(object1)
                #print(loc_check)
                if loc_check is not None:
                    if len(loc_check.ents)!=0:
                        loc_check=loc_check.ents[0].label_
                        if loc_check == 'GPE':
                            string1 = sentence.replace(object1,"which location")
                            ans=object1
                            flag=1
                    
             #if no location kinda question then normal way   
            if flag==0:
                #print(subject)
                #print(object1)
                #print(sentence)
                if(sub_type in ['PRP','NNP']):
                    string1 = sentence.replace(subject,"who")
                elif(sub_type in ['NN']):
                    string1 = sentence.replace(subject,"what")
                ans=subject
                
                #who where when what
                #print("over")
            string1=string1+'?'    
            #print(string1)
        return [string1],[ans]
    
        
    def extractnoun(self,sentence):
        tagged=nltk.pos_tag(sentence.split())
        for pos,pos_type in tagged:
            
            if pos_type in ["NN","NNS","NNP","NNPS","POS"]:
                return pos
        
        
        return ""
        
        
    def extractpronoun(self,sentence):
        tagged=nltk.pos_tag(sentence.split())
        for pos,pos_type in tagged:
            
            
            if pos_type in ["PRP","WP"]:
                return pos
            else:
                pass
        return "" 
    def extractverb(self,sentence):
        tagged=nltk.pos_tag(sentence.split())
        for pos,pos_type in tagged:
            
            if pos_type in ["VB","VBD","VBG","VBN","VBP","VBZ"]:
                return pos
            else:
                pass
        return ""
    def extractadjective(self,sentence):
        tagged=nltk.pos_tag(sentence.split())
        for pos,pos_type in tagged:
            
            if pos_type in ["JJ","JJR","JJS"]:
                return pos
            else:
                pass
                
        return ""
    def extractadverb(self,sentence):
        tagged=nltk.pos_tag(sentence.split())
        for pos,pos_type in tagged:
            
            if pos_type in ["WRB","RB","RBR","RBS"]:
                return pos
            else:
                pass
        return ""
    
#solution=helper()
#print(solution.questionator("naeem is awesome"))
