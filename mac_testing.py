import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="88c338261bec42df85520844f3efc019",
    client_secret="a7154f6308ff4fb082455f9035703e9a",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-playback-state user-modify-playback-state"
))

# Trigger a request to force token caching
me = sp.me()
print(f"✅ Authenticated as: {me['display_name']}")