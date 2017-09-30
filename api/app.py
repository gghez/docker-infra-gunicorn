from pymongo import MongoClient
client = MongoClient('mongo', 27017)
messages = client.superdb.messages

def _init():
    if len(list(messages.find())) == 0:
        msg = {'text': 'Message from mongo'}
        messages.insert_one(msg)

def app(environ, start_response):
    _init()

    data = bytes(messages.find_one()['text'] + '\n', 'utf-8')
    status = "200 OK"
    headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(data)))]
    start_response(status, headers)
    return iter([data])

