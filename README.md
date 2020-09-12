---
vimeoId: 95beec91a4
---

# vgs_test
Small Flask application to demonstrate VGS functionality of tokenizing financial information as well as detokenizing it.

First off, go to https://www.verygoodsecurity.com/ and sign up for a trial account to use as it will be needed to work obviously.

Next, for the code to work you must export the following environmental variables in your .bashrc file or follow https://mcpmag.com/articles/2019/03/28/environment-variables-in-powershell.aspx to set them via Powershell.  
    +HTTPS_PROXY_USERNAME='Username'  </br>
    +HTTPS_PROXY_PASSWORD='Password'  </br>
    +TENANT_ID='Tenant ID'  <br>
    +PATH_TO_VGS_PEM='Your Path to File Here' </br>
    ^^^^ You can find the cert here https://www.verygoodsecurity.com/docs/guides/outbound-connection   
To install, clone this repo wherever you choose.
Open it and run pip3 install -r requirements.txt to get requirements satisfied.
Run python3 app.py and navigate to localhost:5000 </br>

{% include vimeoPlayer.html id=page.vimeoId %}

