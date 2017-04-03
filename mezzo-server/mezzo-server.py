import os
import config
import sys
import logging
import datetime
import tornado.web
import tornado.ioloop
import tornado.options
import random
import handlers

DEBUG = True
DIRNAME = os.path.dirname(os.path.abspath(__file__))

STATIC_PATH = os.path.join(DIRNAME, 'static')
TEMPLATE_PATH = os.path.join(DIRNAME, 'template')
logging.debug(DIRNAME)

settings = {
    'debug': DEBUG,
    'template_path': TEMPLATE_PATH,
    'static_path': STATIC_PATH
    }

db = {'database':'dummy'}

application = tornado.web.Application([
    (r"/", handlers.MainHandler),
    (r"/admin", handlers.AdminHandler),
    (r"/dev", handlers.DeviceHandler),
    # (r"/", BrowserHandler),
    # (r"/add", AddUserHandler),
    # (r"/remove", RemoveUserHandler),
    # (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": STATIC_PATH}),
], db=db, **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    logging.debug('now listening on 8888')
