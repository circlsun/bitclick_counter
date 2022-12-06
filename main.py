import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(token, url):
    headers = {'Authorization': f"Bearer {token}"}
    url_shorten = "https://api-ssl.bitly.com/v4/shorten"
    payload = {
        "long_url": url
    }
    response = requests.post(url_shorten, headers=headers, json=payload)
    return response.json()["id"]


def count_clicks(token, bitlink):
    headers = {"Authorization": f"Bearer {token}"}
    params = (
        ("units", "-1"),
    )
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    response = requests.get(url, headers=headers, params=params)
    return response.json()["total_clicks"]


def is_bitlink(token, url):
    headers = {'Authorization': f"Bearer {token}"}
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    response = requests.get(url, headers=headers)
    return response.ok


def get_bitly_token():
    load_dotenv()
    try:
        token = os.environ["BITLY_TOKEN"]
        return token
    except KeyError:
        print("Дополните виртуальное окружение токеном bitly")


def main():
    token = get_bitly_token()
    url = input("Введите ссылку: ")
    if token:
        try:
            if is_bitlink(token, url):
                print("Число кликов по ссылке:", count_clicks(token, url))
            else:
                print('Битлинк:', shorten_link(token, url))
        except requests.exceptions.HTTPError:
            print("Введите корректную ссылку")


if __name__ == "__main__":
    main()
