import os
import tweepy
from dotenv import load_dotenv
from Utils.helpers import getJuego

contador = 0

# Cargar credenciales del archivo .env
load_dotenv()

api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Autenticación
client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_KEY_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
)

def test(indice):
    tweet = getJuego(indice)
    response = client.create_tweet(text=tweet)
    print("Tweet publicado:", response.data)