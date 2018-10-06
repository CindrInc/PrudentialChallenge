import urllib
import urllib.request as requests

#[ base url: https://developer.api.yodlee.com/ysl , api version: 1.1 ]
response = requests.urlopen("https://developer.api.yodlee.com/ysl ")
print(response.read())

CO_BRAND_LOGIN:'sbCobdcddf2bf509e1bd18aba3e09326e978d8a'
CO_BRAND_PASSWORD:"f12a5508-147e-4913-82e8-2c535d9874c0"
