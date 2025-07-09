import os
import tweepy
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv
from datetime import datetime

contador = 0

# Cargar credenciales del archivo .env
load_dotenv()

api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Autenticación
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def publicar_tweet():
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje = f"Este es un tweet automático de prueba. Hora: {ahora}"
    try:
        api.update_status(mensaje)
        print("Tweet publicado:", mensaje)
    except Exception as e:
        print("Error al publicar tweet:", e)

# Planificador
scheduler = BlockingScheduler()
scheduler.add_job(publicar_tweet, 'cron', hour=19, minute=0)  # Hora local

print("Bot iniciado. Esperando para twittear a las 19:00...")
scheduler.start()
