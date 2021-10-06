import time
import schedule
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

import base64
with open("C:\\Users\\You\\YourWorkingDirectory\\Data\\PlaylistPhoto.jpeg", "rb") as img_file:
    myimage = base64.b64encode(img_file.read())

print("Starting Playlist updater")
  
def func():
    scope = 'playlist-modify-public ugc-image-upload'

    # Spotify Username
    username = 'username'

    # Spotify Developer App Client ID and Secret ID
    SPOTIPY_CLIENT_ID = 'clientid'
    SPOTIPY_CLIENT_SECRET = 'clientsecret'

    token = util.prompt_for_user_token(username,scope,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,redirect_uri='http://yourdomain.com')
    sp = spotipy.Spotify(auth=token)

    # Playlist Data
    id = 'https://open.spotify.com/playlist/yourplaylist'
    playlist_name = 'Playlist Name'
    playlist_description = 'Playlist Description'
    image_b64 = myimage

    sp.playlist_upload_cover_image(playlist_id=id, image_b64 = myimage)
    sp.user_playlist_change_details(username, id, name=playlist_name, description=playlist_description)

    print("Playlist updated")

schedule.every(5).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(30)
    continue 
