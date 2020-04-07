import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():

    with open('books.json') as json_file:
        data = json.load(json_file)

    return jsonify(data)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    name = query_parameters.get('name')
    age = query_parameters.get('age')

    data = {}
    returnItem = []

    with open('books.json') as json_file:
        data = json.load(json_file)

    for p in data['people']:
        if p['age'] == int(age):
            returnItem.append(p)

    return jsonify(returnItem)

app.run()