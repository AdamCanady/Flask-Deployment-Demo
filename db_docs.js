use flaskdemo;
db.dropDatabase();

use flaskdemo;

db.articles.insert({
  "title": "Carleton Is The Best!!",
  "content": "<p>At Carleton, the folks are wonderful and they have a great time coming to <a href=\"http://devx.io\">DevX</a>!</p>"
});

db.articles.insert({
  "title": "DevX is awesome!",
  "content": "<p>At Carleton, the folks are wonderful and they have a great time coming to <a href=\"http://devx.io\">DevX</a>!</p>"
});