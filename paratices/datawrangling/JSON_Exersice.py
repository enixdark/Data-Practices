import json
import requests
import pprint
import ast

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    data = ast.literal_eval(json.loads(requests.get(url).text.strip()))
    return data['topartists']['artist'][0]['name'] # return the top artist in Spain