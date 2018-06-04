
import requests


def get_api(url):
    return requests.get(url).text


def get_ss_status():
    return get_api('http://192.168.10.1:5000/ss/status')