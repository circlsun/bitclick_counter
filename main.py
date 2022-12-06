import requests
import os
from dotenv import load_dotenv


def shorten_link(token, url):
    headers = {'Authorization': f"Bearer {token}"}
    url_shorten = "https://api-ssl.bitly.com/v4/shorten"
    payload = {
        "long_url": url
    }
    response = requests.post(url_shorten, headers=headers, json=payload)
    bitlink = response.json()["id"]
    return bitlink


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
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return False
    return True


def main():
    token = os.getenv('BITLY_TOKEN')
    load_dotenv()
    url = input("Введите ссылку: ")
    if not is_bitlink(token, url):
        try:
            bitlink = shorten_link(token, url)
        except requests.exceptions.HTTPError:
            print("Введите корректную ссылку")
        else:
            print('Битлинк:', bitlink)
    else:
        try:
            print("Число кликов по ссылке:", count_clicks(token, url))
        except requests.exceptions.HTTPError:
            print("Введите корректную ссылку")



if __name__ == "__main__":
    main()
