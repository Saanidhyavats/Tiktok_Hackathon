"""
Artist DataBase

Columns: Track ID (Primary Key), Artist ID, Genre tags

"""

import sqlite3
import random


def create_inf_table():
  # Connect to SQLite database (or create it if it doesn't exist)
  conn = sqlite3.connect('inf.db')
  cursor = conn.cursor()

  # Create the Tracks table
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS ARTIST (
      TikTokID INTEGER PRIMARY KEY,
      Like INTEGER,
      Country TEXT,
      Genre TEXT
  )
  ''')

  # Commit changes and close connection
  conn.commit()
  conn.close()

def insert_inf(num_rows=1000):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('inf.db')
    cursor = conn.cursor()

    # Define genre tags and artist IDs
    genre_tags = ['jazz', 'rock', 'classical', 'hip-hop', 'historic', 'instrumental', 'international', 'blues']
    artist_ids = range(1, 51)  # Artist IDs from 1 to 50

    # Prepare data
    data = []
    for i in range(1, num_rows + 1):
        TikTokID = i
        Like = random.randint(10000, 100000)
        Country = random.choice(['USA', 'Canada', 'UK', 'Australia', 'India'])
        genre = random.choice(genre_tags)
        data.append((TikTokID, Like, Country, genre))

    # Insert data
    cursor.executemany('INSERT OR REPLACE INTO ARTIST (TikTokID, Like, Country, Genre) VALUES (?, ?, ?, ?)', data)

    # Commit changes and close connection
    conn.commit()
    conn.close()
