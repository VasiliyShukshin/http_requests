import requests
import json


def get_hero_powerstats(hero_name, characteristics):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url=url)
    list_heros = json.loads(response.text)
    for hero in list_heros:
        if hero["name"] == hero_name:
            id = hero["id"]
            url2 = f"https://akabab.github.io/superhero-api/api/powerstats/{id}.json"
            response2 = requests.get(url=url2)
            hero_powerstats = json.loads(response2.text)
            hero_character = {hero["name"]: hero_powerstats[characteristics]}
            # print(hero_character)
    return hero_character


def who_is_smarter(*args):
    start_dict = {}
    for arg in args:
        cleverest = get_hero_powerstats(arg, "intelligence")
        start_dict.update(cleverest)
        max_value = max(start_dict.values())
        final_dict = {k: v for k, v in start_dict.items() if v == max_value}
    print(final_dict)


who_is_smarter("Hulk", "Captain America", "Thanos", "Apocalypse")
