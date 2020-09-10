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
    #Following along with 
    res = requests.post('http://bdbdbacbd292.ngrok.io/send',json=info_to_secure)
    res=res.json()
    return res

if __name__ == '__main__':
    #https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https
    app.run()

