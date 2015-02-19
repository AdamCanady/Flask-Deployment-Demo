from flask import Flask, render_template, request, redirect
import pymongo

db = pymongo.MongoClient().flaskdemo

app = Flask(__name__)
app.debug = True

@app.route("/")
def display_news():
    articles = list(db.articles.find())
    return render_template('home.html', articles = articles)

@app.route("/new_post", methods=['POST'])
def new_post():
    article = {
        'title': request.form['title'],
        'content': request.form['body'],
    }
    db.articles.insert(article)
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)