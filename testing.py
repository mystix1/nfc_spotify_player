import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="88c338261bec42df85520844f3efc019",
    client_secret="a7154f6308ff4fb082455f9035703e9a",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-playback-state user-modify-playback-state"
))

devices = sp.devices()

if devices['devices']:
    print("🟢 Available Spotify Devices:")
    for d in devices['devices']:
        print(f"- {d['name']} (ID: {d['id']}) — Active: {d['is_active']}")
else:
    print("🔴 No active Spotify devices found. Make sure your Pi shows up in Spotify and is selected.")