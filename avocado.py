from flask import Flask
import random

facts_list = ["Technology addiction involves excessive use of technology that leads to problems and distress","Some of the common types of technology addiction include Internet gaming","Some of the common types of technology addiction Social media","To play gaming allot can couse Lying to friends, family or loved ones about their frequency of using technology.","To game to much time a day can couse you thinking about technological use, having cravings, and/or spending tremendous amounts of time engaging with a technology."]
coin = ["head","tail"]
code = ["0","9","8","7","6","5","4","3","2","1"]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f'<h1>all intrasting facts you can find by going this link</h1><a href="/random-facts">link to random fun fact</a>'

@app.route("/secret")
def secret():
    return f'<h1>you found a secret page</h1><h2>if you drop a computer coin it will be :</h2><p>{random.choice(coin)}</p><h2>that is a random code</h2><p>{random.choice(code)}</p> <p>{random.choice(code)}</p> <p>{random.choice(code)}</p> <p>{random.choice(code)}</p> <p>{random.choice(code)}</p> <p>{random.choice(code)}</p> <p>{random.choice(code)}</p> <p>{random.choice(code)}</p>'



@app.route("/pepa-pig")
def pepa_pig():
    return f'<h3>more ditaild information you can find on this site</h3><a href="https://www.psychiatry.org/patients-families/technology-addictions-social-media-and-more">more information</a>'

@app.route("/apple")
def apple():
    return "<h1>hellecopter hellecoppter hellecopter</h1>"

@app.route("/banana")
def banana():
    return "<h2>baby yoda baby yoda banana banana</h2>"

@app.route("/random-facts")
def randomfacts():
    return f'<p>{random.choice(facts_list)}</p>'


app.run(debug=True, use_reloader=False)









