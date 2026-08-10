from flask import Flask, render_template, request
import os, requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/form", methods=["POST"])
def form():
    return render_template('form.html')

@app.route('/playlists', methods=["POST"])
def playlists():
    mood = request.form["mood"].strip().lower()
    weather = request.form["weather"].strip().lower()
    activities = request.form["activities"].strip().lower()
    query = f"{mood} {weather} {activities} songs"
    url = f"https://www.googleapis.com/youtube/v3/search"
    params = {"part":"snippet", "q": query, "type":"playlist", "maxResults":5, "key":api_key}
    response = requests.get(url, params=params, timeout=5)
    data = response.json()
    if "error" in data:
        return "Error: Please try again later."
    results = []
    for item in data["items"]:
        results.append({"title": item["snippet"]["title"],"thumbnail": item["snippet"]["thumbnails"]["default"]["url"],"channel": item["snippet"]["channelTitle"],"url":f"https://www.youtube.com/playlist?list={item['id']['playlistId']}"})
    return render_template('playlists.html', results=results)

if __name__== '__main__':
    app.run()