import requests

languages = {}


data = requests.get("https://www.duolingo.com/2017-06-30/users?username=PetraLang6")
data_json = data.json()['users'][0]

for course in data_json['courses']:
    languages[course['title']] = course['learningLanguage']

print(languages)

print(languages['German'])
print(list(languages.keys())[list(languages.values()).index('de')])