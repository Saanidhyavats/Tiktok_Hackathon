"""
Artist DataBase

Columns: Track ID (Primary Key), Artist ID, Genre tags

"""

import sqlite3
import random
import numpy as np


def create_artist_table():
  # Connect to SQLite database (or create it if it doesn't exist)
  conn = sqlite3.connect('artist.db')
  cursor = conn.cursor()

  # Create the Tracks table
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS Tracks (
      TrackID INTEGER PRIMARY KEY,
      ArtistID INTEGER,
      GenreTags TEXT
  )
  ''')

  # Commit changes and close connection
  conn.commit()
  conn.close()

def insert_artist(num_rows=1000):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('artist.db')
    cursor = conn.cursor()

    # Define genre tags and artist IDs
    genre_tags = ['rock', 'pop', 'jazz', 'classical', 'hip-hop', 'electronic', 'country', 'blues', 'reggae', 'alternative']
    artist_ids = range(1, 51)  # Artist IDs from 1 to 50

    # Prepare data
    data = []
    for i in range(1, num_rows + 1):
        track_id = i
        artist_id = random.choice(artist_ids)
        genres = ','.join(random.sample(genre_tags, k=random.randint(1, 3)))  # Randomly choose 1 to 3 genres
        data.append((track_id, artist_id, genres))

    # Insert data
    cursor.executemany('INSERT OR REPLACE INTO Tracks (TrackID, ArtistID, GenreTags) VALUES (?, ?, ?)', data)

    # Commit changes and close connection
    conn.commit()
    conn.close()




"""
User DataBase

Columns: Track ID (Primary Key), User ID, f10, f20, f30, f40, f50, f60, f70, f80, f90, f100, Country

f- frequency of play

"""

def create_user_table():
  conn = sqlite3.connect('user.db')
  cursor = conn.cursor()

  cursor.execute('''
  CREATE TABLE IF NOT EXISTS USER2 (
      sno INTEGER PRIMARY KEY,
      Track_ID INTEGER,
      User_ID INTEGER,
      f10 INTEGER,
      f20 INTEGER,
      f30 INTEGER,
      f40 INTEGER,
      f50 INTEGER,
      f60 INTEGER,
      f70 INTEGER,
      f80 INTEGER,
      f90 INTEGER,
      f100 INTEGER,
      Country TEXT
  )
  ''')

  conn.commit()
  conn.close()

# Function to generate random user data
def generate_random_user_data():
    # Connect to the database
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()

    # Insert 10,000 random records into the USER table
    for i in range(10000):
      # Generate random user data
        Track_ID = np.random.randint(1, 10)  # Track ID will be auto-incremented
        User_ID = np.random.randint(1, 10000)
        f10 = np.random.randint(1, 100)
        f20 = np.random.randint(1, 100)
        f30 = np.random.randint(1, 100)
        f40 = np.random.randint(1, 100)
        f50 = np.random.randint(1, 100)
        f60 = np.random.randint(1, 100)
        f70 = np.random.randint(1, 100)
        f80 = np.random.randint(1, 100)
        f90 = np.random.randint(1, 100)
        f100 = np.random.randint(1, 100)
        country = np.random.choice(['USA', 'Canada', 'UK', 'Australia', 'India'])
        cursor.execute('''
        INSERT OR REPLACE INTO USER2 (sno, Track_ID, User_ID, f10, f20, f30, f40, f50, f60, f70, f80, f90, f100, Country)
        VALUES (?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', [i, Track_ID, User_ID, f10, f20, f30, f40, f50, f60, f70, f80, f90, f100, country])

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

"""SQL Queries"""
import pandas as pd
def query(TrackID, Frequency=None, Country=None):
  # CASE I: TrackID, Frequency, and Country are given
  if (TrackID != None and Frequency != None and Country != None):
    query = f"SELECT * FROM USER2 WHERE Track_ID = {TrackID} AND {Frequency}>0 AND Country = '{Country}'"
    c = 1
  # CASE II: TrackID and Frequency are given
  elif (TrackID != None and Frequency != None):
    query = f"SELECT * FROM USER2 WHERE Track_ID = {TrackID} AND {Frequency}>0"
    c = 1
  # CASE III: TrackID is given
  elif (TrackID != None and Country != None):
    query = f"SELECT * FROM USER2 WHERE Track_ID = {TrackID} AND Country = '{Country}'"
    c = 2
  # CASE IV: TrackID is given
  elif (TrackID != None):
    query = f"SELECT * FROM USER2 WHERE Track_ID = {TrackID}"
    c = 2
  #return query
  conn = sqlite3.connect('user.db')
  cursor = conn.cursor()
  cursor.execute(query)
  records = cursor.fetchall()
  records= pd.DataFrame(records, columns = ["sno","tid","uid","f10", "f20", "f30", "f40", "f50", "f60", "f70", "f80", "f90", "f100", "country"])
  return records, c



def counts(records,frequency,c):
    if c == 1:
        ind = 0
        counts = []
        for _ in range(20):
            counts.append(records[(records[f"{frequency}"]>ind) & (records[f"{frequency}"]<ind+5)][f"{frequency}"].count())
            ind += 5
    if c == 2:
        ind = 0
        counts = []
        for frequency in ["f10","f20","f30","f40","f50","f60","f70","f80","f90","f100"]:
            count = []
            ind = 0
            for _ in range(20):
                count.append(records[(records[f"{frequency}"]>ind) & (records[f"{frequency}"]<ind+5)][f"{frequency}"].count())
                ind += 5
            counts.append(count)
    return counts