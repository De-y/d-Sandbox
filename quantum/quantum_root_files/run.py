import requests

url = 'http://localhost:5000/post/'
myobj = {
  "title": "Post1 updated",
  "published": False,
  "authorId": 1
}


x = requests.post(url, json = myobj)

print(x.text)
