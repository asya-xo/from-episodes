#file that talks to the fandom API

#import library we installed
import requests


def fetch_episodes():
    #fandom API endpoint for fetching data about episodes
    url = "https://from.fandom.com/api.php"

    #telling the api exactly what we want (episodes in json format)
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": "Category:Episodes",
        "cmlimit": "500",
        "format": "json"
    }

    #response.json() converts the response into Python readable data (a dictionary)
    response = requests.get(url, params=params)
    data = response.json()

    return data

#fetch details about episodes

def fetch_episode_details(title):
    url = "https://from.fandom.com/api.php"

    params = {
        "action": "query",
        "titles": title,
        "prop": "categories",
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data