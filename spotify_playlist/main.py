import requests
from bs4 import BeautifulSoup
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

client_id = os.environ.get('SPOTIFY_CLIENT_ID')
client_secret = os.environ.get('SPOTIFY_SECRET')
spotify_username = os.environ.get('MY_USERNAME')

# print(f'client id: {client_id}\nclient secret: {client_secret}\nUsername: {spotify_username}')

# TODO 1 scrape song title information from billboard website using the specific date as an input
# Ask for input of date

date: str
date = input('Enter a date to check out the 100 Hot Lists in format YYYY-MM-DD: \n')

billboard_url = 'https://www.billboard.com/charts/hot-100/' + date

# 2000-08-12
response = requests.get(billboard_url)

# Create beautiful soup
soup = BeautifulSoup(response.text, 'html.parser')

music_class = 'c-title'
titles = soup.select('li ul li h3')
# print(titles)

# song_list is the list of the titles of the songs
# artist_list is the list of artists

song_list = [song.getText().strip() for song in titles]
# artists = soup.select('li ul li span')
artists = soup.find_all(name='span', class_='lrv-u-font-size-14@mobile-max')
artist_list = [artist.getText().strip() for artist in artists]
# print(song_list)
# print(len(song_list))
# print(artist_list)
# print(len(artist_list))

# TODO 2 use the spotify api to create a playlist with the data from 1 above

# Get access token from spotify
# client_id = 'a3ab4559dde84c3b9b39be071d72d99e'
# client_secret = '2a1ad07ba5194bf4a2e42b8c8ccd7740'
redirect_uri = 'http://localhost:3000/'
# spotify_username = 'deedadey'
scope = 'playlist-modify-public playlist-modify-private playlist-read-private'

# credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# Create another spotipy object which is well authenticated to create playlist.
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret,
                                               redirect_uri=redirect_uri, scope=scope,
                                               username=spotify_username))
# Use the credentials to create a spotipy object
track_name = 'Shape of You'
# spotify = spotipy.Spotify(client_credentials_manager=credentials)

result = sp.search(q=track_name, type='track', limit=1)
# print(result)
# print(result['tracks']['items'][0]['album']['artists'][0]['uri'])
# print(result['tracks']['items'][0]['name'])
# print(result['tracks']['items'][0]['uri'])

# spotify.search(q=music, type='track', limit=1)['tracks']['items'][0]['uri']
playlist_data = [sp.search(q=music, type='track', limit=1)['tracks']['items'][0]['uri'] for music in song_list]
print(playlist_data)

playlist = sp.user_playlist_create(sp.me()['id'], name=f'top 100 {date}', public=True,
                                   description=f'top 100 hot billboard songs for {date}')

# print(playlist['id'])

add_tracks = sp.playlist_add_items(playlist['id'], playlist_data)
