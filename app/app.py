from flask import Flask
from flask import render_template, request
import requests
import json
import os

app = Flask(__name__)

USERNAME = os.environ.get('HTTPS_PROXY_USERNAME')
PASSWORD = os.environ.get('HTTPS_PROXY_PASSWORD')
TENANT_ID = os.environ.get('TENANT_ID')
PATH_TO_VGS_PEM = os.environ.get('PATH_TO_VGS_PEM')

#https://stackoverflow.com/questions/54150762/i-want-to-make-pretty-json-formatting-in-flask
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


def helper_func_redacted_data():
    #Helper funciton I made to clean up the generate route as it was and still is handling too much.
    #Basically takes credit card form fields and makes it JSON to send for tokenization
    card_number = request.form['number']
    expiration = request.form['expiry']
    cvv_code = request.form['cvv']
    info_to_secure = {
        "card_number": card_number,
        "expiration": expiration,
        "cvv_code": cvv_code
    }

    #Generated with Postman during testing
    url = "https://tntkp8h2mvu.sandbox.verygoodproxy.com/post"
    payload = json.dumps(info_to_secure)
    headers = {
        'Authorization': 'Basic YXBwbGVzZWVkY2FzdDBAZ21haWwuY29tOkZyb2RvITIz',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    #I've tried to make it pretty but nothing has worked yet.
    json_data = json.loads(response.text)
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
    tokenized_data = helper_func_redacted_data()
    os.environ[
        'HTTPS_PROXY'] = "https://{}:{}@{}.SANDBOX.verygoodproxy.com:8080".format(
            USERNAME, PASSWORD, TENANT_ID)

    res = requests.post('https://echo.apps.verygood.systems/post',
                        json=tokenized_data,
                        verify=PATH_TO_VGS_PEM)
    json_unredacted = json.loads(res.text)
    #This processes the form and returns a JSON k,v pair
    return render_template('redacted.html',
                           tokenized=tokenized_data['data'],
                           detokenized=json_unredacted["json"]["json"])


if __name__ == '__main__':
    app.run()
