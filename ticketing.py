import os
import requests
from dotenv import load_dotenv

load_dotenv()

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")
TRELLO_LIST_ID = os.getenv("TRELLO_LIST_ID")


def create_trello_ticket(title: str, description: str) -> dict:
    if not all([TRELLO_API_KEY, TRELLO_TOKEN, TRELLO_LIST_ID]):
        raise RuntimeError("Trello credentials are not set")

    url = "https://api.trello.com/1/cards"
    params = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN,
        "idList": TRELLO_LIST_ID,
        "name": title,
        "desc": description,
    }

    r = requests.post(url, params=params, timeout=15)
    if r.status_code != 200:
        raise RuntimeError(f"Trello error {r.status_code}: {r.text}")

    return r.json()
