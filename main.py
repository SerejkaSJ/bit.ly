import requests
import argparse
import json
import os

from dotenv import load_dotenv
TOKEN = os.getenv("TOKEN")


def create_short_link(token, link):
    headers = {'Authorization': token}
    payload = {
        "long_url": link,
    }
    response = requests.post('https://api-ssl.bitly.com/v4/bitlinks', headers = headers, json=payload)
    return json.loads(response.text)['link']


def get_summary_link(token, link):
    headers = {'Authorization': token}
    response = requests.get('https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(link), headers = headers)
    return json.loads(response.text)['total_clicks']


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("link")
    args = parser.parse_args()
    your_link = args.link
    try:
        print(get_summary_link(TOKEN, your_link))
    except json.decoder.JSONDecodeError:
        your_link = 'https://' + your_link
        print(create_short_link(TOKEN, your_link))
    except KeyError:
        print(create_short_link(TOKEN, your_link))
