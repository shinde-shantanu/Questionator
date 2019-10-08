# review by Naeem dated 8th August 2019 
#This is very redundant code which was intended to generate captions, metadata, description, url of sports images from sports Website. This produces a json file.
import requests
import json


def crawler():
	
	for page in range (1,2):

			url = ('https://newsapi.org/v2/everything?'
										 'sources=football-italia,bbc-sport,bleacher-report,four-four-two,fox-sports,the-sport-bible&'
										 'q=football OR soccer&'
										 'pageSize=100&'
										 'page='+str(page)+'&'
										 'apiKey=c2ad965df9c141ee9ab7c00e0050a0f6')

			response = requests.get(url)
			from pprint import pprint
			pprint (response.json())


			with open('data'+str(page)+'.txt', 'w') as outfile:  
					json.dump(response.json(), outfile,indent=4)
	return response.json()
crawler()

#This not utilised for the current version of Questionator api 
