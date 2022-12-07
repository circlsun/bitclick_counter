import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    headers = {
        'Authorization': f"Bearer {token}"
    }
    url_shorten = "https://api-ssl.bitly.com/v4/shorten"
    payload = {
        "long_url": url
    }
    response = requests.post(url_shorten, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(token, bitlink):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = (
        ("units", "-1"),
    )
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(token, url):
    headers = {
        'Authorization': f"Bearer {token}"
    }
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    try:
        token = os.environ["BITLY_TOKEN"]
        user_url = input("Введите ссылку: ")
        parsed_url = urlparse(user_url)
        bitlink = f"{parsed_url.netloc}{parsed_url.path}"

        try:
            if is_bitlink(token, bitlink):
                print("Число кликов по ссылке:", count_clicks(token, bitlink))
            else:
                print('Битлинк:', shorten_link(token, user_url))
        except requests.exceptions.HTTPError:
            print("Введите корректную ссылку")

    except KeyError:
        print("Дополните виртуальное окружение токеном от bitly")


if __name__ == "__main__":
    main()
