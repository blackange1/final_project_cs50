import requests

response = requests.get('http://go.mail.ru')
try:
    doc=response.content.decode('utf-8',errors='ignore')
except:
    doc=response.content.decode('cp1251',errors='ignore')

print(doc)
doc = requests.get('https://wooordhunt.ru/word/have').content.decode('utf-8',errors='ignore')