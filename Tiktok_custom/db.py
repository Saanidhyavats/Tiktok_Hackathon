"""
Artist DataBase

Columns: Track ID (Primary Key), Artist ID, Genre tags

"""

import sqlite3
import random
import numpy as np

genres=[{'song': 'Arne Huseby - Warm Duck Shuffle', 'genre': 'Blues'}, {'song': 'Blind Boy Paxton - Mind Reader Blues (Live @ KEXP)', 'genre': 'Blues'}, {'song': 'Bombay Laughing Club - Workin Boy Blues', 'genre': 'Blues'}, {'song': 'Brother JT - Child of the Sun', 'genre': 'Blues'}, {'song': 'Brother JT - Hey Mr. Sun', 'genre': 'Blues'}, {'song': 'Brother JT - Interview', 'genre': 'Blues'}, {'song': 'Brother JT - Nothing Really', 'genre': 'Blues'}, {'song': 'Delta Dreambox - Queen of Loneliness', 'genre': 'Blues'}, {'song': 'F J Blues - The Message', 'genre': 'Blues'}, {'song': 'F J Blues - Unknown Man', 'genre': 'Blues'}, {'song': 'Ignatz - She Gets All That She Wants', 'genre': 'Blues'}, {'song': "Little Howlin' Wolf - Baltimore Raven", 'genre': 'Blues'}, {'song': "Little Howlin' Wolf - Blue Coochology", 'genre': 'Blues'}, {'song': 'Loren Connors and Bill Orcutt - Untitled 4', 'genre': 'Blues'}, {'song': "Nobody's Bizness - Come on in My Kitchen", 'genre': 'Blues'}, {'song': "Nobody's Bizness - Sittin' on Top of the World", 'genre': 'Blues'}, {'song': "Paul Wine Jones - Don't Laugh At Me", 'genre': 'Blues'}, {'song': 'Paul Wine Jones - If You Love Me Like You Say', 'genre': 'Blues'}, {'song': 'Paul Wine Jones - Nobody But You', 'genre': 'Blues'}, {'song': 'Paul Wine Jones - Pucker Up, Butter Cup', 'genre': 'Blues'}, {'song': 'Paul Wine Jones - Stop Arguing', 'genre': 'Blues'}, {'song': 'Roger McGuinn - 500 Miles', 'genre': 'Blues'}, {'song': 'Roger McGuinn - Joshua Fit the Battle of Jericho', 'genre': 'Blues'}, {'song': "T-Model Ford - Dust My Broom (live in the Kutsher's Country Club lobby)", 'genre': 'Blues'}, {'song': 'Wildbirds and Peacedrums - Doubt_Hope', 'genre': 'Blues'}, {'song': 'Wildbirds and Peacedrums - There Is No Light', 'genre': 'Blues'}, {'song': 'Achachak - 01 First Movement.mp3', 'genre': 'Classical'}, {'song': 'Achachak - Fifth Movement', 'genre': 'Classical'}, {'song': 'Achachak - First Movement', 'genre': 'Classical'}, {'song': 'Achachak - Fourth Movement', 'genre': 'Classical'}, {'song': 'Achachak - Second Movement', 'genre': 'Classical'}, {'song': 'Achachak - Third Movement (1)', 'genre': 'Classical'}, {'song': 'Achachak - Third Movement', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 01', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 02', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 03', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 04', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 05', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 07', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 08', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 10', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 11', 'genre': 'Classical'}, {'song': 'Brakhage - 40th Mantra (Instrumental)', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - 40th Mantra', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - 41st Mantra (Bonus)', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - Le Vrai (Instrumental)', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - Le Vrai ft. Ibou', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - No Coincidence (Instrumental)', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - The Strike', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - This Love (Instrumental)', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - Bad Trip', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - Delete', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - Endorphin Release', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - Nerves', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - Resident Evil', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - War with Yourself', 'genre': 'Hip-Hop'}, {'song': 'JsoundLAB - Soulful Calm Hip Hop', 'genre': 'Hip-Hop'}, {'song': '31 de Octubre - Milongueros', 'genre': 'Historic'}, {'song': 'Artur Aravidi - Rise (Epic, Inspirational, Cinematic)', 'genre': 'Historic'}, {'song': "Billy Murray - Are you the O'Reilly_", 'genre': 'Historic'}, {'song': 'Emin Efendi - Hale Makame', 'genre': 'Historic'}, {'song': 'Georgian State Folk Song and Dance Ensemble - Chakrulo', 'genre': 'Historic'}, {'song': 'Henry Burr - The girl from the U.S.A.', 'genre': 'Historic'}, {'song': 'Isidore Soucy - Quadrille Laurier (6ème Partie)', 'genre': 'Historic'}, {'song': 'Islam Yusufov - Song About Stalin', 'genre': 'Historic'}, {'song': 'J. O. LaMadeleine (& Jeannette) - Petite Lili Valse', 'genre': 'Historic'}, {'song': 'Jackson F. Smith - Cantina Rag', 'genre': 'Historic'}, {'song': 'John J. Kimmel - Medley of straight jigs', 'genre': 'Historic'}, {'song': 'Julio J. Martínez Oyanguren - Jota', 'genre': 'Historic'}, {'song': 'Levon Hampartzoumian - Menk Arghez Zinvor', 'genre': 'Historic'}, {'song': 'Parush Parushev - Nazko', 'genre': 'Historic'}, {'song': 'Performer not given. - [Piano solo--march]. (160 rpm)', 'genre': 'Historic'}, {'song': 'Polk Miller and his Old South Quartet - Jerusalem Mournin', 'genre': 'Historic'}, {'song': 'Rizeli Sadık - Erkek Kadın Oyun Havası', 'genre': 'Historic'}, {'song': 'Sam Castandet et son Orchestre Antillais - La Rue Zabyme', 'genre': 'Historic'}, {'song': "Seneca Indians - Children's Chorus", 'genre': 'Historic'}, {'song': 'Seneca Indians - Funeral Chant', 'genre': 'Historic'}, {'song': 'Septeto Machín - El Guateque', 'genre': 'Historic'}, {'song': 'Skarvelis, Kavouras, Peristeris - Pono, De Me Lypasai', 'genre': 'Historic'}, {'song': 'Stapleton Brothers - Call of the Whip-Poor-Will', 'genre': 'Historic'}, {'song': 'Tamburacı Osman Pehlivan - Anadolu Kaşık Havası', 'genre': 'Historic'}, {'song': 'Tefanake, Reia, and Moratai - Ute', 'genre': 'Historic'}, {'song': 'Will F. Denny - Uncle Harry, what is love_ (144 rpm)', 'genre': 'Historic'}, {'song': 'Zainab Palvanova - Ofarin', 'genre': 'Historic'}, {'song': 'Hawkin - Woods', 'genre': 'Instrumental'}, {'song': 'Horse Lords - Outer East', 'genre': 'Instrumental'}, {'song': 'Il Sogno Del Marinaio - Animal Farm Tango', 'genre': 'Instrumental'}, {'song': "Il Sogno Del Marinaio - Nanos' Waltz", 'genre': 'Instrumental'}, {'song': 'Il Sogno Del Marinaio - Partisian Song', 'genre': 'Instrumental'}, {'song': 'Il Sogno Del Marinaio - Verse IX', 'genre': 'Instrumental'}, {'song': 'Raul Diaz Palomar - Abdalá (demo, bonus)', 'genre': 'Instrumental'}, {'song': 'SalmonLikeTheFish - Glacier', 'genre': 'Instrumental'}, {'song': 'SalmonLikeTheFish - Sequoia', 'genre': 'Instrumental'}, {'song': 'SalmonLikeTheFish - Shenandoah', 'genre': 'Instrumental'}, {'song': 'SalmonLikeTheFish - Yellowstone', 'genre': 'Instrumental'}, {'song': 'SalmonLikeTheFish - Zion', 'genre': 'Instrumental'}, {'song': 'will austin - Reverie Solo Dec 2016a', 'genre': 'Instrumental'}, {'song': 'will austin - Reverie Solo Dec 2016b', 'genre': 'Instrumental'}, {'song': 'Dengue Fever - No Sudden Moves', 'genre': 'International'}, {'song': 'Dengue Fever - Sober Driver', 'genre': 'International'}, {'song': 'Judith Cohen - La muerte del Duque de Gandía', 'genre': 'International'}, {'song': 'Watcha Clan - Spanish Civil War Tribute', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - Boki Trinaest', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - Kozarica Kolo', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - Mig Mig', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - Prodzo Selo', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - [interview] (1)', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - [interview]', 'genre': 'International'}, {'song': 'Ainst Char - Your Cellar, My Shrine', 'genre': 'Jazz'}, {'song': 'Albert Beger - Point of No Return', 'genre': 'Jazz'}, {'song': 'Albert Beger - Shasha', 'genre': 'Jazz'}, {'song': 'Barnacled - Polyurethane', 'genre': 'Jazz'}, {'song': 'Barnacled - Title', 'genre': 'Jazz'}, {'song': 'Breuss Arrizabalaga Quintet - Ghosts', 'genre': 'Jazz'}, {'song': 'Breuss Arrizabalaga Quintet - Pensamiento', 'genre': 'Jazz'}, {'song': 'Breuss Arrizabalaga Quintet - The Dark Side Of Frigiliana', 'genre': 'Jazz'}, {'song': 'HCI - partial autochthon', 'genre': 'Jazz'}, {'song': 'HCI - washing walls', 'genre': 'Jazz'}, {'song': 'Li Zenghui - soprano saxphone', 'genre': 'Jazz'}, {'song': 'Sid Peacock - Seagull choking on a ring pull', 'genre': 'Jazz'}, {'song': 'Sid Peacock - Want', 'genre': 'Jazz'}, {'song': 'Till Paradiso - Friends will be Friends (TP 70)', 'genre': 'Jazz'}, {'song': 'Till Paradiso - New Ideas (TP 76)', 'genre': 'Jazz'}, {'song': 'Here Comes A Big Black Cloud!! - Black Mold', 'genre': 'Rock'}, {'song': 'Here Comes A Big Black Cloud!! - Death March', 'genre': 'Rock'}, {'song': 'Here Comes A Big Black Cloud!! - The Fly Pt. II', 'genre': 'Rock'}, {'song': 'Matte Black - Loch', 'genre': 'Rock'}, {'song': 'Matte Black - Lungs', 'genre': 'Rock'}, {'song': 'Rod - Inner Guitars', 'genre': 'Rock'}, {'song': 'Rod - Sursaut', 'genre': 'Rock'}, {'song': 'The New Lines - Please Fall In Love', 'genre': 'Rock'}, {'song': 'The New Lines - Sentry On Patrol', 'genre': 'Rock'}, {'song': 'The New Lines - Year Of The Nines', 'genre': 'Rock'}]
# friends = {userid: [str(np.random.choice(10)) for i in range(np.random.choice(10))] for userid in range(1, 11)}
friends={1: ['9', '4', '2', '5', '3'], 2: [], 3: ['9', '5', '6', '8', '2', '7', '1', '4'], 4: ['1', '6', '7', '3','5'], 5: ['7', '3', '2', '6', '8', '4', '1'], 6: ['2', '5', '4', '1'], 7: ['8', '6', '5', '8', '2', '3'], 8: ['2', '9', '1', '8', '7', '6'], 9: ['6'], 10: ['1', '6', '7', '0', '2', '10', '0']}
user_id=5
"""
Artist DataBase

Columns: Track ID (Primary Key), Artist ID, Genre tags

"""

def create_song_table():
  # Connect to SQLite database (or create it if it doesn't exist)
  conn = sqlite3.connect('song.db')
  cursor = conn.cursor()

  # Create the Tracks table
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS Tracks (
      sno INTEGER PRIMARY KEY,
      TrackID INTEGER,
      USERID INTEGER,
      FRIENDS TEXT,
      GenreTag INTEGER,
      score DECIMAL
  )
  ''')

  # Commit changes and close connection
  conn.commit()
  conn.close()

def insert_song(num_rows=100):
    users = 10
    # friends = {userid: [str(np.random.choice(users)) for i in range(np.random.choice(10))] for userid in range(users)}
    # Connect to SQLite database (or create it if it doesn't exist)
    global friends
    conn = sqlite3.connect('song.db')
    cursor = conn.cursor()

    # Define genre tags and artist IDs
    artist_ids = range(1, 51)  # Artist IDs from 1 to 50

    # Prepare data
    data = []
    for i in range(1, num_rows + 1):
        sno = i
        track_id = np.random.choice(100)
        user_id = np.random.choice(users)
        friends_ids = ','.join(friends[user_id+1])
        genretag = genres[sno]["genre"]
        score = np.random.choice([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
        data.append((sno, track_id, user_id, friends_ids, genretag, score))

    # Insert data
    cursor.executemany('INSERT OR REPLACE INTO Tracks (sno, TrackID, USERID, FRIENDS, GenreTag, score) VALUES (?, ?, ?, ?, ?, ?)', data)

    # Commit changes and close connection
    conn.commit()
    conn.close()


create_song_table()
insert_song()

def get_user_tracks():
    # Connect to the database
    conn = sqlite3.connect("song.db")
    cursor = conn.cursor()

    # Prepare and execute the query to fetch all trackid and userid pairs
    query = "SELECT TrackID, USERID, score FROM Tracks"
    cursor.execute(query)

    # Fetch the results
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    # Transform the results into the desired dictionary format
    user_tracks = {}
    for trackid, userid, score in rows:
        if userid not in user_tracks:
            user_tracks[userid] = []
        user_tracks[userid].append([trackid,score])

    return user_tracks

def user_matrix():
    global user_id
    users = set(range(1,11))
    # friends = {userid: [str(np.random.choice(10)) for i in range(np.random.choice(10))] for userid in range(1, 11)}
    # trial_user=np.random.randint(1,11)
    trial_user=3
    friend_of_user=friends[trial_user]
    user_tracks=get_user_tracks()
    print(user_tracks)
    song_of_user=[i[0] for i in user_tracks[trial_user]]
    
    all_songs=[]+song_of_user
    for i in friend_of_user:
        for j in user_tracks[int(i)]:
           if j[0] not in all_songs:
                all_songs.append(j[0])
    all_users= [str(trial_user)]+friend_of_user

    user_matrix= np.zeros((len(all_users),len(all_songs)))
    for i in range(len(all_users)):
        for j in range(len(all_songs)):
            k=[l[0] for l in user_tracks[int(all_users[i])]]
            z= [l[1] for l in user_tracks[int(all_users[i])]]
            if all_songs[j] in k:
                user_matrix[i][j]=z[k.index(all_songs[j])]*9
            else:
                user_matrix[i][j]=0

    genre_user=[0]*8
    genre_recommend=[False]*8
    for i in song_of_user:
        if genres[i]['genre']=='Blues':
            genre_user[0]+=1
        elif genres[i]['genre']=='Hip-Hop':
            genre_user[1]+=1
        elif genres[i]['genre']=='International':
            genre_user[2]+=1
        elif genres[i]['genre']=='Rock':
            genre_user[3]+=1
        elif genres[i]['genre']=='Historic':
            genre_user[4]+=1
        elif genres[i]['genre']=='Jazz':
            genre_user[5]+=1
        elif genres[i]['genre']=='Classical':
            genre_user[6]+=1
        elif genres[i]['genre']=='Instrumental':
            genre_user[7]+=1
    temp=['Blues','Hip-Hop','International','Rock','Historic','Jazz','Classical','Instrumental']
    threshold=max(genre_user)*0.2
    for i in genre_user:
        if i<threshold:
            genre_recommend[i]=temp[i]
    return np.array(user_matrix), genre_recommend, all_songs,threshold,genre_user


# song_of_user= set(song_of_user)

# song_of_friend=set()
# for i in friend_of_user:
#     for j in user_tracks[int(i)]:
#         song_of_friend.add(j)

# all_songs= set()
# all_songs = song_of_user.copy()
# all_songs.update(song_of_friend)
# print('all_songs',all_songs)

# friend_of_user= [str(trial_user)]+friend_of_user
# print('friend_of_user',friend_of_user)

# user_matrix= np.zeros((len(friend_of_user),len(all_songs)))
# for i in range(len(friend_of_user)):
#     for j in range(len(all_songs)):
#          if all_songs(j) in user_tracks(int(friend_of_user[i])):
#             user_matrix[i][j]=1
#          else:
#              user_matrix[i][j]=0
print(user_matrix())
