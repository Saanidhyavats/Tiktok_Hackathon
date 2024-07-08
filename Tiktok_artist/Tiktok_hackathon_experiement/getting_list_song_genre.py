import os

def get_songs_with_genres(base_dir):
    songs_with_genres = []

    for genre in os.listdir(base_dir):
        genre_path = os.path.join(base_dir, genre)
        if os.path.isdir(genre_path):
            for song in os.listdir(genre_path):
                song_path = os.path.join(genre_path, song)
                if os.path.isfile(song_path):
                    songs_with_genres.append({
                        'song': song[:-4],
                        'genre': genre
                    })

    return songs_with_genres

# Define the base directory containing the genre folders
base_dir = 'Genre'

# Get the list of songs with their genres
songs_with_genres = get_songs_with_genres(base_dir)

# Print the list of songs with their genres
print(songs_with_genres)
