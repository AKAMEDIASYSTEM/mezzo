import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	# this is the recurring "show current status" req
    	# poll device-disabled-statuses and return properly-formatted template
        self.write("I AM MEZZO\rYOU ARE MINE")

    def post(self):
    	# this is the "update device-disabled list" req
    	# look at payload and alter device-disabled-status list as needed
        self.write("I AM MEZZO\rYOU ARE MINE")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()