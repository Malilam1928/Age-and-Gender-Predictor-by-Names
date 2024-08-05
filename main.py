from flask import Flask, render_template
import random
from datetime import datetime
import requests
GENDERIZER_URL = "https://api.genderize.io?"
AGIFY_URL = "https://api.agify.io?"

app = Flask(__name__)



@app.route('/')
def home():
    current_date = datetime.now()
    current_year = current_date.year
    random_number = random.randint(1,10)
    return render_template("index.html",num=random_number, year=current_year)
@app.route("/guess/<name>")
def identity(name):
    def gender(name):
        name_param = {
            "name": name,
        }
        response = requests.get(url=GENDERIZER_URL, params=name_param)
        results = response.json()
        gender = results.get('gender', 'Unknown')
        return gender

    def age(name):
        name_param = {
            "name": name,
        }

        response = requests.get(url=AGIFY_URL, params=name_param)
        results = response.json()
        age = results.get('age', 'Unknown')
        return age
    return render_template("guess.html", gender=gender(name),age=age(name),name=name)

if __name__ == "__main__":
    app.run(debug=True)


