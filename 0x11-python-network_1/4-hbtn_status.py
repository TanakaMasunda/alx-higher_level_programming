#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status.use request packages"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(content(r.text)))
