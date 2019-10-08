import pandas as pd
import os
import json
from  POShelper import Helper
data=pd.read_csv("summary.csv")
# path to summary.csv to be given to get the summarised news articles
h=Helper()
startindex="N_"
index=0
json_str={}
#question,ans=questionator("A was born in B")
class json_gen():
    def automate(self,
                 ans):
            
        json_str["sentence"] = ans
        #json_str["id"]=startindex+str(index)
        #index=index+1
        #qa={}
        #qa["question"],qa["answer"]=h.questionator(ans)
        features={}
        features[h.extractnoun(ans)] = "noun"
        features[h.extractpronoun(ans)] = "pronoun" 
        features[h.extractverb(ans)] = "verb"
        features[h.extractadjective(ans)] = "adjective" 
        features[h.extractadverb(ans)] = "adverb" 
        
        json_str["features"] = features
        json_str["question"],json_str["answer"]=h.questionator(ans)
        #print(type(json.dumps(json_str)))
        success={}
        final_json={}
        success["code"]="200"
        success["message"]= "Question successfully generated"
        success["data"]=json_str
        final_json["success"]=success
        return json.dumps(final_json)
        
        
#j = json_gen()    
#print(j.automate("Naeem is a very nice boy"))
            
    
#uncomment the function call to generate the json make sure that there is already available data.json empty file
#j=json_gen()
#print(j.automate())
    



