import os
import config
import sys
import logging
import datetime
import tornado.web
import tornado.ioloop
import random

DEBUG = True
DIRNAME = os.path.dirname(os.path.abspath(__file__))

STATIC_PATH = os.path.join(DIRNAME, 'static')
TEMPLATE_PATH = os.path.join(DIRNAME, 'template')
print DIRNAME
print STATIC_PATH
print TEMPLATE_PATH

settings = {
    'debug': True,
    'template_path': TEMPLATE_PATH,
    'static_path': STATIC_PATH
    }

db = {'database':'dummy'}

class MainHandler(tornado.web.RequestHandler):
    # def initialize(self):
    #     self.static_path = 'foo'

    def get(self):
    	# this is the recurring "show current status" req
    	# poll device-disabled-statuses and return properly-formatted template
        print STATIC_PATH
        devices = [{'dev':'alexa','devType':'speechTranscript', 'timeTillReactivate':200},
        {'dev':'echo','devType':'audioRecord', 'timeTillReactivate':200},
        {'dev':'dropcam','devType':'camera', 'timeTillReactivate':200}]
        loader = tornado.template.Loader('templates')
        self.write(loader.load('swipeTemplate.html').generate(devices=devices))

    def post(self):
    	# this is the "update device-disabled list" req
    	# look at payload and alter device-disabled-status list as needed
        self.write("I AM MEZZO\rYOU ARE MINE")

application = tornado.web.Application([
    (r"/", MainHandler),
    # (r"/submit", SubmitHandler),
    # (r"/", BrowserHandler),
    # (r"/add", AddUserHandler),
    # (r"/remove", RemoveUserHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": STATIC_PATH}),
], db=db, **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
