import flask
from flask import Flask
import pymongo

db = pymongo.MongoClient().flaskdemo

app = Flask(__name__)
app.debug = True

@app.route("/")
def display_news():
    articles = db.articles.find()

    return flask.render_template('main.html', articles = articles)

@app.route("/new_post", methods=['POST'])
def new_post():
  pass

if __name__ == "__main__":
    app.run()