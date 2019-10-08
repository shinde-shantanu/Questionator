import tornado.ioloop
import tornado.web
import json
from gen_option import mk_option

class MainHandler(tornado.web.RequestHandler):
    
    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    def post(self):
       	ip = self.get_argument("answer")
        output = mk_option(ip)
        output = output[:4]
        self.write(json.dumps(output))
	

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(6505)
    tornado.ioloop.IOLoop.current().start()
