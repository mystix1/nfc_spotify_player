# player.py
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

# Spotify Auth Setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="88c338261bec42df85520844f3efc019",
    client_secret="a7154f6308ff4fb082455f9035703e9a",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-playback-state user-modify-playback-state",
    cache_path=".cache"
))

# Your Raspotify device ID
DEVICE_ID = "4df2d4d453aabeb45a23ccec5057f600ee7b7d12"

# Load registry
with open("registry.json", "r") as f:
    registry = json.load(f)

reader = SimpleMFRC522()

try:
    while True:
        print("Waiting for you to scan an RFID sticker/card")
        card_id = str(reader.read()[0])
        print("The ID for this card is:", card_id)

        if card_id in registry:
            uri = registry[card_id]["spotify_uri"]
            print(f"🎵 Playing: {registry[card_id]['name']}")
            sp.transfer_playback(device_id=DEVICE_ID, force_play=True)
            sleep(1)
            sp.start_playback(device_id=DEVICE_ID, context_uri=uri)
            sleep(2)
        else:
            print("❌ Card ID not found in registry.")

finally:
    GPIO.cleanup()
