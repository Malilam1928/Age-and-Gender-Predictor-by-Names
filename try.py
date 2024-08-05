import requests

GENDERIZER_URL = "https://api.genderize.io?"
AGIFY_URL = "https://api.agify.io?"
def gender(name):
    name_param = {
        "name":name,
    }

    response = requests.get(url=GENDERIZER_URL, params=name_param)
    results = response.json()
    gender = results.get('gender', 'Unknown')
    return print(gender)

def age(name):
    name_param = {
        "name" :name,
    }

    response = requests.get(url=AGIFY_URL,params=name_param)
    results = response.json()
    age = results.get('age','Unknown')
    return print(age)

gender("mali")
age("mali")