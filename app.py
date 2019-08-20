# import dependencies
from flask import Flask
from flask import request
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import pymongo
import scrape_mars

# FLASK SETUP. Create an app, being sure to pass __name__
app = Flask(__name__)

# Connect to MongoDB
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.mars_db
collection = db.items

# Flask Routes
@app.route("/scrape")
def scrape():
    return scrape_mars


if __name__ == "__main__":
    app.run(debug=True)
