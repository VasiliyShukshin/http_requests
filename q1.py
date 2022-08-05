import requests
from pprint import pprint
import json

def get_hero_powerstats(hero_name, characteristics):
    # print(type(args))
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url=url)
    list_heros = json.loads(response.text)
    for hero in list_heros:
        # # pprint(hero)
        # print(hero["name"])
        # print(args)
        # print(type(args))
        if hero["name"] == hero_name:
            # print(hero["name"])
            id = hero["id"]
            # print(id)
            response2 = requests.get(url=f"https://akabab.github.io/superhero-api/api/powerstats/{id}.json")
            hero_powerstats = json.loads(response2.text)
            # print(hero_powerstats)
            # print(hero_powerstats[characteristics])
            hero_character = {hero["name"] : hero_powerstats[characteristics]}
            # print(hero_character)
    return hero_character
#
def who_is_smarter(*args):
    start_dict ={}
    for arg in args:
        cleverest = get_hero_powerstats(arg, "intelligence")
        start_dict.update(cleverest)
        # print(start_dict)
        max_value = max(start_dict.values())
        final_dict = {k: v for k, v in start_dict.items() if v == max_value}
    print(final_dict)
#     hero_powerstats = get_hero_powerstats("Thanos")
#     intelligence = hero_powerstats["intelligence"]
#     print(intelligence)
#
#
# who_is_smarter()
# get_hero_powerstats("Thanos", "intelligence")
who_is_smarter("Hulk", "Captain America", "Thanos", "Apocalypse")