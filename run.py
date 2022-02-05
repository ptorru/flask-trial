from flask import Flask, render_template
from urllib.request import urlopen
import json

import argparse
app = Flask(__name__)


@app.route("/")
def template_test():
    key = app.config.get('key')
    with urlopen("https://api.nasa.gov/planetary/apod?api_key="+key) as myurl:
        response = myurl.read()
    data = json.loads(response)

    moreimgs = app.config.get('random')
    if moreimgs != None:
        with urlopen("https://api.nasa.gov/planetary/apod?count="+str(moreimgs)+"&api_key="+key) as myurl:
            data2 = myurl.read()
        others = json.loads(data2)
    else:
        others = []

    return render_template('template.html', title=data["title"], mystring="Wheeeeee!", explain=data["explanation"], mylist=[90,1,2,3,4], picurl=data["hdurl"], others=others)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Runs a simple flask web server.')
    parser.add_argument('apikey', metavar='apikey', type=str,
                        help="API key for Nasa's API service.")
    parser.add_argument('random', metavar='random', type=int,
                        help='number of extra images to get.')

    args = parser.parse_args()
    app.config['key'] = args.apikey
    app.config['random'] = args.random

    app.run(debug=True, port=5055)
