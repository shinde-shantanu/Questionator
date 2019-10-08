1. Author Name: Naeem
2. Version No.1
3. Research Title: using nltk and coreNLP to do Natural Language processing
4. Features


for this there is a requirement of install the stanford core NLP modules from the official documentation.
after this go into the folder and then run the following command in the command prompt

##java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000


thus we have managed to set up our CoreNLp server

now you can verify and run all the functions in automate.py :)

after this onto the json generation.This is done by running the file sever_api.py

=======
To download the Stanford CoreNLP :- 

# https://stanfordnlp.github.io/CoreNLP/download.html

the  run the server go the stanford CoreNLP folder and type the command in the terminal :- 

# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000
>Now once we have the stanford NLTK Server Running in the background, Let's Move onto the Running the API. Now first run the requirements

```python
pip install -r requirements.txt
```
After installing all the dependencies, now run the python api file
```python
python sever_api.py
```
Once this is set up you are done with the setting up this api. Do make sure that the stanford NLTK server are running in the background. That's all from my side.


#THANK YOU
