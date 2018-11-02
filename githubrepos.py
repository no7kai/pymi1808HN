import requests
import json
import sys

username = sys.argv[1]
r = requests.get('https://api.github.com/users/{}/repos'.format(username))
data = r.json()
for repo in data:
    print(repo['name'])

