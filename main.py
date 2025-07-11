import argparse

from itadScraper import scrapearITAD
from Utils.helpers import getJuego
from twitterBot import *

if __name__ == "__main__":
    scrapearITAD()
    parser = argparse.ArgumentParser()
    parser.add_argument("--indice", type=int, required=True)
    args = parser.parse_args()
    test(args.indice)