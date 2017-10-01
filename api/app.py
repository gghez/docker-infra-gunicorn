import logging

from pymongo import MongoClient
from flask import Flask, request


app = Flask(__name__)

client = MongoClient('mongo', 27017)
messages = client.superdb.messages

def _init():
    logging.info('_init')

    if len(list(messages.find())) == 0:
        msg = {'text': 'Message from mongo'}
        messages.insert_one(msg)

@app.route('/')
def get_message():
    _init()

    logging.info('remote address: %s', request.remote_addr)
    logging.info('req headers: %r', request.headers)

    data = messages.find_one()['text']

    return data

