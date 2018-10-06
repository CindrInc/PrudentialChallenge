#from urllib.request import Request, urlopen
import requests
import json


#[ base url: https://developer.api.yodlee.com/ysl , api version: 1.1 ]


CO_BRAND_LOGIN = 'sbCobdcddf2bf509e1bd18aba3e09326e978d8a'
CO_BRAND_PASSWORD = "f12a5508-147e-4913-82e8-2c535d9874c0"

data = {
    "cobrand":{
        "cobrandLogin":CO_BRAND_LOGIN,
        "cobrandPassword":CO_BRAND_PASSWORD,
        "locale":"en_US"
        }
    "Authorization":
}

headers = {'Api-Version': '1.1','Cobrand-Name': 'restserver','Content-Type': 'application/json'}

data_json = json.dumps(data)
req = requests.get("https://developer.api.yodlee.com/ysl/transactions/count", headers = headers, data = data_json)

print(req.text)

# GET  HTTP/1.1ß
# Host:
# Connection: keep-alive
# Accept: application/json
# Origin: https://developer.yodlee.com
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36
# Authorization: {cobSession=08062013_0:a85b10c7d99cadaed03363dba4f9c5d9db0fbe38feebd5e749f67a61b64d5b1f02abbc2a294f3179bcbfa15fe8eac08292035b32128403fca134134b98226a53,userSession=08062013_2:e0af3dab005bc1a33915c5f486d2465ff08dfe65dd233bdc4c9ec0a908e580e7198323eea76f002420eed1ba7e3b974acff1979b3329b18953dab534cd0bf5b6}
# Api-Version: 1.1
# Cobrand-Name: restserver
# Referer: https://developer.yodlee.com/apidocs/index.php
# Accept-Encoding: gzip, deflate, sdch, br
# Accept-Language: en-US,en;q=0.8
