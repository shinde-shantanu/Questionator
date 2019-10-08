from spcyques import create_questions
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            ip=self.get_argument('sen')
            obj={}
            obj["features"],obj["question"],obj["answer"]=create_questions(ip)
            
            op={}
            op["code"]="200"
            op["message"]="question generated successfully"
            op["data"]=obj

            op_o={}
            op_o["success"]=op
            self.write(op_o)
        except Exception as e:
            op={}
            op["error"]={"code":"400",
                         "message":str(e)}
            self.write(op)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
