# coding: utf-8
import json
import logging
from flask import Flask

formatter = logging.Formatter(u'%(message)s')
logger = logging.getLogger()

if not logger.handlers:
    handler = logging.StreamHandler()
else:
    handler = logger.handlers[0]

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Create flask server
APP = Flask(__name__)
APP.debug = True

@APP.route('/')
def hello():
    return u"Hello World"
