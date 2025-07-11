import argparse

from bot.scraper import scrapearITAD
from bot.twitter import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--indice", type=int, required=True)
    args = parser.parse_args()
    publicarTweet(args.indice)