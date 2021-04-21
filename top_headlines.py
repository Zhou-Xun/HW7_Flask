from flask import Flask, render_template, request
from secrets import api_key
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'

@app.route('/name/<name>')
def name(name):
    return render_template('name.html', name=name)

@app.route('/headlines/<name>')
def headlines(name):
    base_url = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    params = {"api-key": api_key}
    response = requests.get(base_url, params)
    results = response.json()['results'][:5]
    hls = [res['title'] for res in results]

    return render_template('headlines.html', name=name, hls=hls)


@app.route('/links/<name>')
def extra1(name):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {'api-key': api_key}
    response = requests.get(base_url, params)
    results = response.json()['results'][:5]
    hls_urls = [{'title': res['title'], 'url': res['url']} for res in results]
    print(hls_urls)
    return render_template('extra1.html', name=name, hls_urls=hls_urls)


@app.route('/images/<name>')
def extra2(name):
    base_url = 'https://api.nytimes.com/svc/topstories/v2/technology.json'
    params = {'api-key': api_key}
    response = requests.get(base_url, params)
    results = response.json()['results'][:5]
    total_info = [{'title': res['title'], 'url': res['url'], 'image': res['multimedia'][1]['url']} for res in results]

    return render_template('extra2.html', name=name, total_info=total_info)

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)