from flask import Flask
from flask import render_template
from flask import render_template, request, jsonify
import requests
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

@app.route('/send', methods=['GET','POST'])
def get_form_info():
    card_number = request.form['number']
    expiration = request.form['expiry']
    cvv_code=request.form['cvv']
    info_to_secure = {"card_number":card_number,"expiration":expiration,"cvv_code":cvv_code}

if __name__ == '__main__':
    app.run()

