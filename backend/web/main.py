from flask import Flask
from flask import json
from flask import Response

from digger.databases import core
from digger.databases import cedet
from digger.databases import loja_integrada

app = Flask(__name__)

@app.route('/') 
def hello_world(): 
    return 'Hello, World!'

@app.route('/<bookStore>/book/<bookName>', methods=['GET']) 
def getStoreBooks(bookStore,bookName):
    getBook = core.getBookStore(bookStore) 
    js = json.dumps(getBook(bookName))
    resp = Response(js, status=200, mimetype='application/json')
    return resp