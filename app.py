from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_news"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
        latest_news = mongo.db.latest_news.find_one()
        return render_template("index.html", latest_news=latest_news)
        '''news_title=latest_news.news_title
        ,news_p = latest_news.news_p
        ,featured_image_url = latest_news.featured_image_url
        ,mars_weather = latest_news.mars_weather
        ,mars_facts = latest_news.mars_facts
        ,img_list = latest_news.hemisphere_image_urls)
        '''



@app.route("/scrape")
def scraper():
    latest_news = mongo.db.latest_news
    latest_news_data = scrape_mars.scrape()
    latest_news.update({}, latest_news_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)