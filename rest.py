import urllib.request, json
import requests
# Opening a web request
url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=n&apiKey=f8b6d0027c4bfafdeabc")
# Decoding response to str
data = json.loads(url.read().decode()) # Decoding a web request
requests.get('https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=n&apiKey=f8b6d0027c4bfafdeabc')
# Parsing results
results = data['results']
USD_ILS = results['USD_ILS']
val = USD_ILS['val']
print(val)