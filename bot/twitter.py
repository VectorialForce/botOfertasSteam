import os
import sys

import tweepy
from dotenv import load_dotenv
from bot.utils import *

load_dotenv()

api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_KEY_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
)

MAX_INTENTOS = 10

def publicarTweet():

    for intento in range(MAX_INTENTOS):

        try:
            response = client.create_tweet(text=getJuegoAleatorio())
            print(f"Tweet publicado con éxito: {response.data['id']}")
            break
        except tweepy.errors.Forbidden as e:
            if "duplicate content" in str(e).lower():
                print(f"Tweet duplicado para índice, intentando con el siguiente...")
                continue
            else:
                print("Otro tipo de error:", e)
                break
        except tweepy.errors.TooManyRequests as e:
            print("Se alcanzó el límite de publicaciones mensuales")
            print(f"ERROR {e.response.status_code}: {e.response.reason}")
            sys.exit(1)