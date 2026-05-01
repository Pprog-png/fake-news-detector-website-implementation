import requests

API_KEY = open("api_key").read()
SEARCH_ENGINE_ID = open("search_engine_id").read()


def searchnet(search_query):
    url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "q":search_query,
        "key":API_KEY,
        "cx":SEARCH_ENGINE_ID
    }

    response = requests.get(url,params=params)
    response = response.json()
    result = []
    if "items" in response:
        for i in response['items']:
            l = {
                "title":i["title"],
                "snippet" : i["snippet"],
                "link" : i["link"]
            }
            result.append(l)
    return result