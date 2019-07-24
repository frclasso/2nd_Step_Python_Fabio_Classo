import requests

url = 'http://datacamp.com/teach/documentation'

r = requests.get(url)
text = r.text
print(text)