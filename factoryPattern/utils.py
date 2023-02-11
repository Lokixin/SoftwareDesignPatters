import requests

API_ROUTE = "https://api.namefake.com/"


def generate_name() -> str:
    res = requests.get(API_ROUTE)
    return res.json()["name"]


if __name__ == "__main__":
    print(generate_name())
