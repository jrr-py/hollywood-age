#!/bin/venv

"""
jrr-py - github.com/jrr-py/hollywood-age
Apache 2.0 License - apache.org/licenses/LICENSE-2.0.txt
"""

import requests
import sys

# globals
app_version = "0.1"
api_key = ""


def requestData(movie_title):
    url = "https://imdb-api.com/en/API/SearchMovie/" + api_key + "/" + movie_title
    try:
        r = requests.get(url, timeout = 10)
        count = 1
        if r.status_code == 200:
            print(f'-------------------------')
            response = r.json()
            for k in response['results']:
                print(count, k['title'], k['description'])
                count += 1
        selection = input('Select a result, 0 to quit: ')
        if selection == '0':
            finalize()
    except:
        print('Error!')

def finalize():
    finalize_url = "https://imdb-api.com/en/API/Usage/" + api_key
    try:
        r = requests.get(finalize_url, timeout = 10)
        if r.status_code == 200:
            print(f'-------------------------')
            print(r.json())
            sys.exit(0)
    except SystemExit as ex:
        pass

if __name__ == '__main__':
    print(f'///////////////////////////')
    print(f'       hollywood-age')
    print(f'       Version: ' + app_version)
    print(f'///////////////////////////')
    #requestData('PyCharm')
    movie_title = input("Movie title: ")
    requestData(movie_title)