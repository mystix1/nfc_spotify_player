# tag_mapper.py
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json
import time

# Wipe and reset registry.json before scanning
with open("registry.json", "w") as f:
    json.dump({}, f)

# Load empty registry
with open("registry.json", "r") as f:
    registry = json.load(f)

# Album list from notebook
albums = [
    {"name": "Album 1", "spotify_uri": "spotify:album:4SZko61aMnmgvNhfhgTuD3"},
    {"name": "Album 2", "spotify_uri": "spotify:album:3SpBlxme9WbeQdI9kx7KAV"},
    {"name": "Album 3", "spotify_uri": "spotify:album:3r46DPIQeBQbjvjjV5mXGg"},
    {"name": "Album 4", "spotify_uri": "spotify:album:7aObAFaIOcczMSDnfXz5z6"},
    {"name": "Album 5", "spotify_uri": "spotify:album:26ztFK3E69j5THJQdyxC5w"},
    {"name": "Album 6", "spotify_uri": "spotify:album:7eqoqGkKwgOaWNNHx90uEZ"},
    {"name": "Album 7", "spotify_uri": "spotify:album:0S0KGZnfBGSIssfF54WSJh"},
    {"name": "Album 8", "spotify_uri": "spotify:album:5zi7WsKlIiUXv09tbGLKsE"},
    {"name": "Album 9", "spotify_uri": "spotify:album:6MO2bfZ2lD3O6Uie2E9hV6"},
    {"name": "Album 10", "spotify_uri": "spotify:album:7K3zpFXBvPcvzhj7zlGJdO"},
    {"name": "Album 11", "spotify_uri": "spotify:album:1xzBco0xcoJEDXktl7Jxrr"},
    {"name": "Album 12", "spotify_uri": "spotify:album:2gRPz3hzwx1dTWJdRcTjzO"},
    {"name": "Album 13", "spotify_uri": "spotify:album:3dMwC1N8VPSxrPMoIJRdUg"},
    {"name": "Album 14", "spotify_uri": "spotify:album:1mJFgPeuLhUjErKrouf4pH"},
    {"name": "Album 15", "spotify_uri": "spotify:album:3V2Tj2Q5P4Qz3bNzTDMt8d"},
    {"name": "Album 16", "spotify_uri": "spotify:album:1A1e4vF7ooyvEMBbJFM4wZ"},
    {"name": "Album 17", "spotify_uri": "spotify:album:6xgqn8nNuVYtToYXWlTIyx"},
    {"name": "Album 18", "spotify_uri": "spotify:album:1kmyirVya5fRxdjsPFDM05"},
    {"name": "Album 19", "spotify_uri": "spotify:album:6J84szYCnMfzEcvIcfWMFL"},
    {"name": "Album 20", "spotify_uri": "spotify:album:6s84u2TUpR3wdUv4NgKA2j"}
]

reader = SimpleMFRC522()
assigned = 0

try:
    while assigned < len(albums):
        print(f"📡 Scan sticker #{assigned + 1} of {len(albums)}...")
        card_id = str(reader.read()[0])

        if card_id in registry:
            print(f"⚠️ Card {card_id} already assigned to: {registry[card_id]['name']}")
        else:
            registry[card_id] = albums[assigned]
            print(f"✅ Assigned card {card_id} to {albums[assigned]['name']}")
            assigned += 1

            # Save updated registry
            with open("registry.json", "w") as f:
                json.dump(registry, f, indent=4)

        time.sleep(1)

finally:
    GPIO.cleanup()
    print("🧹 Cleaned up GPIO")