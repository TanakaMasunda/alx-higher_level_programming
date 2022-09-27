#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status.use request packages"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    t = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
