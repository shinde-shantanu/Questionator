#This is the production api to be used for the question generation in the questionator website. Whenever you run this api make sure that you run the Stanford Core NLP servers too.
import tornado.ioloop
import tornado.web
from POShelper import Helper
from json_generator import json_gen

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("WELCOME TO THE END GAME")


class QuestionHandler(tornado.web.RequestHandler):
    def post(self):
        sentence = self.get_argument('sentence')
        #print(sentence)
        #h=Helper()
        #question,ans=h.questionator(sentence)
        j=json_gen()
        self.write(j.automate(sentence))
        
        
def make_app():
        return tornado.web.Application([ (r"/", MainHandler),(r"/sentence", QuestionHandler) ],debug=True)  # URL Mapping

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)    # Port Number
    tornado.ioloop.IOLoop.current().start()
