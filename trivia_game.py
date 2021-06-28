import requests

URL="https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=multiple"





#GET, POST, PUSH,DELETE, PARSE

resp=requests.get(URL)

x= resp.json()

print(x)

print (type(x))

print (x["results"][0]["question"])
