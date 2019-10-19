1. Author Name: Shantanu S. Shinde
2. Version No. 2
3. Research Title: Generating questions using named entity racognition and english language grammar rules
4. Features : Generates questions given a sentence as input.

Dependensies-
	1.Spacy
	2.NLTK
	3.json
	4.gensim
	5.tornado
	

Usage-

1.Demo-
python demo.py
Takes sentence as input and prints all possible questions with answers.

2.Create a json file-
python create_json.py
Makes a json 'data.json' file with all questions for entries in the 'summary.csv'

3.Creating a 'summary.csv' file from bbc dataset-
python create_summary.py
Makes a 'summary.csv' file. Change the path in the create_summary.py file to the path for bbc dataset.

<<<<<<< HEAD
API-

python api_c.py
This runs the tornado server to resoond to api requests.

While sending the api request sen a string that is the sentence with a variable name 'sen'.