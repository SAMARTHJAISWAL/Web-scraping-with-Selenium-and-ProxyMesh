from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    TWITTER_USERNAME = "your_twitter_username"
    TWITTER_PASSWORD = "your_twitter_password"
    MONGO_URI = "mongodb://twitterapp:twitterpass@localhost:27017/twitter_trends?authSource=twitter_trends"
