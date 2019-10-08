#Code review by Naeem Patel at 8th August  

#This again is a modified crawl.py file with some minor changes in the newsapi call and json generation changes. 
import requests
import json


def crawler():
  
  for page in range (1,2):
	  url = ('https://newsapi.org/v2/everything?'
					 'sources=espn-cric-info,talksport,the-times-of-india,the-sport-bible,google-news-uk,bbc-sport&'
					 'q=cricket&'
					 'pageSize=100&'
					 'page='+str(page)+'&'
					 'apiKey=c2ad965df9c141ee9ab7c00e0050a0f6')

	  response = requests.get(url)
	  from pprint import pprint
	  pprint (response.json())


	  with open('datacrick'+str(page)+'.txt', 'w') as outfile:  
		  json.dump(response.json(), outfile,indent=4)
  return response.json()

#calling the crawler function
crawler()

#This code is not required if the plan is to run the questionator api and must not be used for production