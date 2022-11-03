import csv
from flask import Flask, jsonify, request

all_movies = []
with open("movies.csv")as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked = []
disliked = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "Sucess"
    })

@app.route("/liked-movies", methods = ["POST"])
def liked_movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    liked.append(movies)
    return jsonify({
        "status": "Success"
    }), 201

@app.route("/disliked-movies", methods = ["POST"])
def disliked_movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    disliked.append(movies)
    return jsonify({
        "status": "Success"
    }), 201

@app.route("/not-watched-movies", methods = ["POST"])
def not_watched_movies():
    movies = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.appned(movies)
    return jsonify({
        "statues": "Success"
    }), 201

if __name__ == "__main__":
    app.run()

