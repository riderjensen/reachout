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
    return '''<h1>Documentation</h1>
                <style>
                    details {
                        background-color: lightblue;
                        padding: 10px;
                        margin: 5px;
                    }
                    div {
                        background-color: white;
                        padding: 5px;
                        margin: 10px;
                    }
                </style>
                <details>
                    <summary><code>/api/v1/resources/books/all</code></summary>
                    <div style="margin-left: 20px">
                        <p>Returns all books</p>
                    </div>
                </details>
                <details>
                    <summary><code>/api/v1/resources/books</code></summary>
                    <div style="margin-left: 20px">
                        <p>Parameters</p>
                        <code>?age=[int]</code>
                        <code>?name=[string]</code>
                    </div>
                </details>
                '''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():

    with open('books.json') as json_file:
        data = json.load(json_file)

    return jsonify(data)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    # name = query_parameters.get('name')
    age = query_parameters.get('age')

    if age: 
        
        data = {}
        returnItem = []

        with open('books.json') as json_file:
            data = json.load(json_file)

        for p in data['people']:
            if p['age'] == int(age):
                returnItem.append(p)

        return jsonify(returnItem)

    else:
        
        return "Error: No id field provided. Please specify an id."

app.run()