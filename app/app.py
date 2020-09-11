from flask import Flask
from flask import render_template, request, jsonify
import requests
import json
import pprint

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

    #Generated with Postman
    url = "https://tntkp8h2mvu.sandbox.verygoodproxy.com/post"
    payload = json.dumps(info_to_secure)
    headers = {'Authorization': 'Basic YXBwbGVzZWVkY2FzdDBAZ21haWwuY29tOkZyb2RvITIz',
    'Content-Type': 'application/json'
              }
    response = requests.request("POST", url, headers=headers, data = payload)
    json_data=response.json()
    return render_template('redacted.html',response=json_data.get('data'))

if __name__ == '__main__':
    app.run()

#pprint.pprint(json_data.get('data'))