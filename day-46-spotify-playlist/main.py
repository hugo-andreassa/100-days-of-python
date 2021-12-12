from pprint import pprint

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

HOT_100_URL = "https://www.billboard.com/charts/hot-100"
CLIENT_ID = "b0d921a3624c4f18a09c3586bf0adaad"
CLIENT_SECRET = "2bd6c979e19c4d3a88edd9bdd5244d91"


def get_billboard_list(dt: str) -> [str]:
    hot_100 = requests.get(f"{HOT_100_URL}/{dt}").text
    soup = BeautifulSoup(hot_100, "html.parser")

    return [tag.text.replace("\n", "") for tag in soup.select("ul li ul li h3")]


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = get_billboard_list(date)

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt")
)
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

