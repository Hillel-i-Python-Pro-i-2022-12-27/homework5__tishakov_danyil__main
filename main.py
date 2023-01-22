import os
import requests
import json


def get_info():
    response = requests.get("http://api.open-notify.org/astros.json")
    with open("info", "w") as file:
        file.write(response.text)
    answer = json.loads(response.text)
    for i in answer["people"]:
        print(i["name"])

def main():
    print(get_info())

if __name__=="__main__":
    main()