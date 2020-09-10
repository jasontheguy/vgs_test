from flask import Flask
from flask import render_template
from flask import render_template, request, jsonify
import requests
import os
import json

app = Flask(__name__)

@app.route('/')
# A little flair splash page
def main_page():
    return render_template("splash.html")

@app.route('/card.html')
def card():
    # This renders the fancy credit card form
    return render_template("card.html")

@app.route('/form')
def get_form_info():
    # This creates a small JSON document which is mostly the standard of API calls
    num = request.form['number']
    expiration = request.form['expiry']
    cvv = request.form['cvv']
    document_as_json={"card_num":num,"cvv":cvv,"exp_date":expiration}
    y = json.dumps(document_as_json)
    return y
if __name__ == '__main__':
    app.run()
