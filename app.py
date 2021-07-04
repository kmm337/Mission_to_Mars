from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# app is the Flask object

# mars_app is the mongo db name for the active mondodb instance. (created in git bash "use mars_app")
# the URI to the mongodb instance is mongodb://localhost:27017/mars_app

# pymongo constructor ties the Flask object app to the mongodb instance using a database URI string
# mongodb_client = PyMongo(app, uri = "mongodb://localhost:27017/mars_app")
# mongodb instance is then referenced as mongo_client.db
# or can assign the URI string to the key MONGO_URI in app.config
# then mongodb_client = PyMongo(app)

# here mongo is the mongodb_client
# the mongodb instance is referenced as mongo.db?
# mars_app is a collection of documents containing data
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# mongo.db.mars_app.find_one() returns the first document in the mars_app collection
@app.route("/")
def index():
   mars = mongo.db.mars_app.find_one()  # gets a mars_app document
   return render_template("index.html", mars=mars) # returns the data in the document using the index.html template

# variable mars points to the mongodb: mongo.db.mars_app
# scraping.scrape_all() - calls the scrape_all function defined in scraping.py and imported as scraping
# returns a dictionary stored in mars_data {
#      "news_title": news_title,
#      "news_paragraph": news_paragraph,
#      "featured_image": featured_image(browser),
#      "facts": mars_facts(),
#      "last_modified": dt.datetime.now()
#    }

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars_app 
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.run()
