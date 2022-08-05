import requests
from pprint import pprint
import json

def get_hero_powerstats(super_hero_neme):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url=url)
    list_heros = json.loads(response.text)
    for hero in list_heros:
        if hero["name"] == super_hero_neme:
            id = hero["id"]
            response2 = requests.get(url=f"https://akabab.github.io/superhero-api/api/powerstats/{id}.json")
            hero_powerstats = json.loads(response2.text)
    return hero_powerstats

def who_is_smarter():
    hero_powerstats = get_hero_powerstats("Thanos")
    intelligence = hero_powerstats["intelligence"]
    print(intelligence)


who_is_smarter()