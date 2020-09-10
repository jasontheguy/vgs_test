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
    # This renders the fancy credit card form. This data is collected on the generate route below:
    return render_template("card.html")

@app.route('/generate', methods=['POST'])
def generate():
    card_number = request.form['number']
    expiration = request.form['expiry']
    cvv_code=request.form['cvv']
    #This below takes the form data, which works when I test it, and basically makes it a tiny JSON doc
    info_to_secure = {"card_number":card_number,"expiration":expiration,"cvv_code":cvv_code}
    #Following along with https://github.com/Stepan-VGS/simple_app_test_vgs/blob/master/app/routes.py, I cannot get this to even pass thru VGS to encode, from looking at the logs.
    #This is where I am having trouble. This is my understanding:
    #1) I create a JSON document/field with sensitive data. That is defined above.
    #2) I send said document to the path that I defined using the ngrok public server endpoint in the VGS dashboard telling it what fields to redact
    #3) I return it to the VGS echo server to show the data revealed
    #res = requests.post('http://bdbdbacbd292.ngrok.io/send',json=info_to_secure)
    #res=res.json()
    #Opening the PR for feedback from devs/support
    return info_to_secure

if __name__ == '__main__':
    app.run()

