from flask import Flask
import pymongo

app = Flask(__name__)

@app.route("/")
def hello():

  
    return render_template('hello.html', articles = articles)

@app.route("/new_post", methods=['POST'])
def new_post():
  pass

if __name__ == "__main__":
    app.run()