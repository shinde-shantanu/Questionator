#This is the Questionator non production api for the two news crawlers. This should not be invoked if developers plan to deploy it in production.
import tornado.ioloop
import tornado.web

from crawl1 import crawler
from crawl import crawler




class MainHandler(tornado.web.RequestHandler):
	def post(self):
		try:
			op={}
			op["code"]="200"
			op["message"]="successfull"
			op["data"]=crawler()
			op_o={}
			op_o["success"]=op
			self.write(op_o)
		except Exception as e:
			op_o={}
			op_o["error"]={"code":"400","message":str(e)}
			self.write(op_o)

def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
	])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
	
#Please avoid using this as there has been no particular testing phase carried out. 