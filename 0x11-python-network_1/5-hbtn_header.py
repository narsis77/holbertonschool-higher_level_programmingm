#!/usr/bin/python3
"""
Script that takes in a URL and displays the value
of the variable X-Request-Id
"""

if __name__ == "__main__":

    import requests
    import sys

    try:
        r = requests.head(sys.argv[1])
        print("{}".format(r.headers['X-Request-Id']))
    except:
        pass