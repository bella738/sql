import urllib.request, json
url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=ILS_USD&compact=n&apiKey=f8b6d0027c4bfafdeabc")
data = json.loads(url.read().decode())

results = data['results']
USD_ILS = results['ILS_USD']
val = USD_ILS['val']

print('Welcome to currency converter')
amount = input('Please enter an amount of Shekeles to convert:')
try:
    print(float(amount)*val,"$")
    print("Thanks for using our currency converter")
except ValueError:
    print("Invalid Choice")