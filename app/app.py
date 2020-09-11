from flask import Flask
from flask import render_template, request
import requests
import json
import os

USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
TENANT_ID = os.environ.get('TENANT_ID')
HTTPS_PROXY = "%s:%s@%s.SANDBOX.verygoodproxy.com:8080".format(USERNAME, PASSWORD, TENANT_ID)

app = Flask(__name__)

#https://stackoverflow.com/questions/54150762/i-want-to-make-pretty-json-formatting-in-flask
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


def helper_func_redacted_data():
    #Helper funciton I made to clean up generate route as it was and still is handling too much.
    #Basically takes credit card form fields and makes it JSON
    card_number = request.form['number']
    expiration = request.form['expiry']
    cvv_code=request.form['cvv']
    info_to_secure = {"card_number":card_number,"expiration":expiration,"cvv_code":cvv_code}
    
    #Generated with Postman during testing
    url = "https://tntkp8h2mvu.sandbox.verygoodproxy.com/post"
    payload = json.dumps(info_to_secure)
    headers = {'Authorization': 'Basic YXBwbGVzZWVkY2FzdDBAZ21haWwuY29tOkZyb2RvITIz',
    'Content-Type': 'application/json'
              }
    response = requests.request("POST", url, headers=headers, data = payload)
    #I've tried to make it pretty but nothing has worked yet. 
    json_data=json.loads(response.text)
    return json_data


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
    JSON_DATA = helper_func_redacted_data()
    #Note: Credentals are public and this is terrible I know. But, I could not get my environmental variable to be read and interpolated for some reason.
    #All of them are in my .bashrc and I sourced it, but it still wasn't playing nice.
    os.environ['HTTPS_PROXY'] = 'http://USeBmD52ku1oFv3S9XVQf9SD:d5c3a2d1-a8fd-4a12-a834-0ef085e3bb31@tntkp8h2mvu.SANDBOX.verygoodproxy.com:8080'
    #This is my public facing API bucket as I couldn't get the echo server to respond properly.
    DETOKENIZED = requests.post('https://2d84d5444b9db4d97485dcd31208da2c.m.pipedream.net/',
                         json=JSON_DATA,
                         verify='/home/flipz/Code/vgs_test/app/cert.pem')
    #This processes the form and returns a JSON k,v pair
    return render_template('redacted.html',response=JSON_DATA['data'], detokenized=DETOKENIZED)

if __name__ == '__main__':
    app.run()

