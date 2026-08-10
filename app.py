from flask import Flask, render_template, request

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
    return render_template("playlists.html")

if __name__== '__main__':
    app.run(debug)