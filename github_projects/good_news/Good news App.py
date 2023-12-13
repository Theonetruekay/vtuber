from flask import Flask, jsonify
import requests
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when the app is run

# Your API key for NewsAPI
API_KEY = 'e02c845c7fc740689e11db20cb56f7be'

@app.route('/good-news')
def get_good_news():
    # Endpoint to fetch news
    url = ('https://newsapi.org/v2/everything?'
           'q=positive OR happy OR inspiring&'
           'sortBy=popularity&'
           'language=en&'
           'apiKey=' + API_KEY)
    
    # Making a request to the NewsAPI
    response = requests.get(url)
    data = response.json()

    # Filtering the first 5 news items
    news_items = data['articles'][:5]

    # Extracting titles and URLs
    good_news = [{'title': item['title'], 'url': item['url']} for item in news_items]

    return jsonify(good_news)

if __name__ == "__main__":
    app.run()
