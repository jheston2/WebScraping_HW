# import necessary libraries
from flask import Flask, render_template
import scrape_mars as scrape

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def echo():
    news_title = scrape.news_title
    news_p = scrape.news_p
    featured_image_url = scrape.featured_image_url
    mars_weather = scrape.mars_weather
    data = scrape.data
    hemisphere_image_urls = scrape.hemisphere_image_urls
    return render_template("index.html", 
        news_title = news_title,
        news_p = news_p,
        featured_image_url = featured_image_url,
        mars_weather = mars_weather,
        data = data,
        hemisphere_image_urls = hemisphere_image_urls
    )


if __name__ == "__main__":
    app.run(debug=True)
