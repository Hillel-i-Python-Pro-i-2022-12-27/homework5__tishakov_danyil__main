import requests

def get_info():
    response = requests.get("http://api.open-notify.org/astros.json")
    with open("info", "w") as file:
        file.write(response.text)
    return response.text

def main():
    print(get_info())

if __name__=="__main__":
    main()