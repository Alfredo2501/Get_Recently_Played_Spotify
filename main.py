import sqlite3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import pytz

# Initialize the Spotipy client with your credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='YOUR_CLIENT_ID',
                                               client_secret='YOUR_CLIENT_SECRET',
                                               redirect_uri='YOUR_REDIRECT_URI',
                                               scope='user-read-recently-played user-read-private'))

# Get the user's information
user_info = sp.current_user()
user_id = user_info['id']
user_country = user_info['country']

# Get the user's recently played tracks
results = sp.current_user_recently_played()

# Define the filename for the SQLite database
db_file = 'recently_played_tracks.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS tracks (
                    track_id TEXT PRIMARY KEY,
                    track_name TEXT,
                    artist_name TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id TEXT PRIMARY KEY,
                    display_name TEXT,
                    country TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS recently_played (
                    track_id TEXT,
                    user_id TEXT,
                    played_at TEXT,
                    user_country TEXT,
                    FOREIGN KEY(track_id) REFERENCES tracks(track_id),
                    FOREIGN KEY(user_id) REFERENCES users(user_id)
                )''')

# Timezone conversion for Mexico
mexico_timezone = pytz.timezone('America/Mexico_City')

# Insert into dimension tables and fact table
for item in results['items']:
    # Track information
    track = item['track']
    track_id = track['id']
    track_name = track['name']
    artist_name = track['artists'][0]['name']

    # Insert into track_dimension
    cursor.execute('''INSERT OR IGNORE INTO tracks (track_id, track_name, artist_name)
                      VALUES (?, ?, ?)''', (track_id, track_name, artist_name))

    # User information
    display_name = user_info['display_name']

    # Insert into user_dimension
    cursor.execute('''INSERT OR IGNORE INTO users (user_id, display_name, country)
                      VALUES (?, ?, ?)''', (user_id, display_name, user_country))

    # Played track information
    played_at = item['played_at']

    # Convert timestamp to Mexico City time
    played_at = datetime.strptime(played_at, "%Y-%m-%dT%H:%M:%S.%fZ")
    played_at = pytz.utc.localize(played_at)
    played_at = played_at.astimezone(mexico_timezone)

    # Insert into played_tracks_fact
    cursor.execute('''INSERT INTO recently_played (track_id, user_id, played_at, user_country)
                      VALUES (?, ?, ?, ?)''', (track_id, user_id, played_at.strftime("%Y-%m-%d %H:%M:%S"), user_country))

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f'Recently played tracks saved to {db_file}')
