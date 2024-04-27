import os
import requests
from flask import Flask, render_template, request
from requests.auth import HTTPBasicAuth

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
URL = "https://accounts.spotify.com/api/token"

app = Flask(__name__)


def get_access_token(CLIENT_ID: str, CLIENT_SECRET: str, URL: str) -> str:
    """
    Retrieves an access token from the Spotify API using the client credentials flow.

    Args:
        CLIENT_ID (str): The client ID for the Spotify application.
        CLIENT_SECRET (str): The client secret for the Spotify application.
        URL (str): The URL of the Spotify token endpoint.

    Returns:
        str: The access token retrieved from the Spotify API.
    """

    data = {"grant_type": "client_credentials"}
    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    response = requests.post(url=URL, data=data, auth=auth)
    access_token = response.json()["access_token"]
    return access_token


def get_tracks(artist: str, access_token: str) -> dict:
    """
    Retrieves the top 5 tracks by the specified artist from the Spotify API.

    Args:
        artist (str): The name of the artist.
        access_token (str): The access token for the Spotify API.

    Returns:
        dict: A dictionary containing information about the top 5 tracks.
    """
    url = "https://api.spotify.com/v1/search"
    query = f"?q=artist%3A{artist}&type=track&market=ID&limit=5"
    full_url = f"{url}{query}"

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(full_url, headers=headers)
    tracks = response.json()["tracks"]["items"]

    return tracks


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        artist = request.form.get("artist")

        access_token = get_access_token(CLIENT_ID, CLIENT_SECRET, URL)
        tracks = get_tracks(artist, access_token)
        return render_template("index.html", tracks=tracks)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
