import os
import config
import sys
import logging
import datetime
import tornado.web
import tornado.ioloop
import tornado.options
import random

class MainHandler(tornado.web.RequestHandler):
    # def initialize(self):
    #     self.static_path = 'foo'

    def get(self):
    	# this is the recurring "show current status" req
    	# poll device-disabled-statuses and return properly-formatted template
        logging.debug('we are in the MainHandler GET function')

        # QUERY DB OF KNOWN DEVICES AND CREATE 'devices' object reflecting state
        # NOTE, should also have an option to 'disable all' or 'restore all'
        devices = [{'dev':'alexa','function':['speechTranscription111','3rd-party cloud'],'loc':'kitchen', 'timeTillReactivate':200},
        {'dev':'echo','function':['audioRecord22','3rd-party-cloud'], 'loc':'livingRoom', 'timeTillReactivate':200},
        {'dev':'dropcam','function':['camera11','audioRecord'], 'loc':'livingRoom', 'timeTillReactivate':200}]
        logging.debug(devices)
        loader = tornado.template.Loader('templates')
        self.write(loader.load('swipeTemplate.html').generate(devices=devices))

class AdminHandler(tornado.web.RequestHandler):
    '''
    Yet-unwritten handler and template for Mezzo setup
    '''

    def get(self):
        # this is the recurring "show current status" req
        # poll device-disabled-statuses and return properly-formatted template
        logging.debug('we are in the MainHandler GET function')

        # QUERY DB OF KNOWN DEVICES AND CREATE 'devices' object reflecting state
        # NOTE, should also have an option to 'disable all' or 'restore all'
        devices = [{'dev':'alexa','function':['speechTranscription111','3rd-party cloud'],'loc':'kitchen', 'timeTillReactivate':200},
        {'dev':'echo','function':['audioRecord22','3rd-party-cloud'], 'loc':'livingRoom', 'timeTillReactivate':200},
        {'dev':'dropcam','function':['camera11','audioRecord'], 'loc':'livingRoom', 'timeTillReactivate':200}]
        logging.debug(devices)
        loader = tornado.template.Loader('templates')
        self.write(loader.load('adminTemplate.html').generate(devices=devices))

    def post(self):
    	# this is the "update device-disabled list" req
    	# look at payload and alter device-disabled-status list as needed
        logging.debug('we are in the MainHandler POST function')
        self.write("I AM MEZZO\rYOU ARE MINE")

class DeviceHandler(tornado.web.RequestHandler):
    '''
    Endpoint for devices to query if they are directly actuated, ie, on 110v connected relays and not being ghosted via iptables
    '''

    def get(self):
        # this is the recurring "show current status" req
        # poll device-disabled-statuses and return properly-formatted template
        logging.debug('we are in the MainHandler GET function')

        # QUERY DB OF KNOWN DEVICES AND CREATE 'devices' object reflecting state
        # NOTE, should also have an option to 'disable all' or 'restore all'
        devices = [{'dev':'alexa','function':['speechTranscription111','3rd-party cloud'],'loc':'kitchen', 'timeTillReactivate':200},
        {'dev':'echo','function':['audioRecord22','3rd-party-cloud'], 'loc':'livingRoom', 'timeTillReactivate':200},
        {'dev':'dropcam','function':['camera11','audioRecord'], 'loc':'livingRoom', 'timeTillReactivate':200}]
        logging.debug(devices)
        loader = tornado.template.Loader('templates')
        self.write(loader.load('swipeTemplate.html').generate(devices=devices))

    def post(self):
        # this is the "update device-disabled list" req
        # look at payload and alter device-disabled-status list as needed
        logging.debug('we are in the MainHandler POST function')
        self.write("I AM MEZZO\rYOU ARE MINE")