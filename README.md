# Music Discovery

## MUSE
Problem Statement
Our goal is to enhance artists' visibility and diversify music streaming options for users.

### Solution
For Artists:

Song Analytics Platform: Artists can enter a Track ID for analysis, revealing how many users have listened to varying percentages (10%, 20%, ..., 100%) of their song and the frequency of listens. This platform offers options for Country, TrackID, and Percentage/Frequency, with TrackID being mandatory.

Influencer Analytics Platform: Artists can search for influencers by Country and Genre. By leveraging data from the Song Analytics Platform, artists can identify trending regions and collaborate with influencers from these regions to boost their song's popularity. 

These features can be made available in the premium version of TikTok for artists.

For Users:

Local Diversity Recommendation System: Users can create a Friends Network and discover diverse music from their friends' playlists. The system recommends music from genres the user has either "never heard" or "least heard," encouraging exploration beyond their usual interests. This recommendation system uses collaborative filtering with advanced algorithm, suggesting the top four highest-rated predicted songs from different genres listened to by friends. Recommendation system will orient itself according to the user behavior. (The idea behind suggesting diverse song from a friends playlist is that user will more likely listen to that music)

### Tools and Technologies
Tools: Google Colaboratory, VSCode <br>
Libraries/Modules: Sqlite3, Pandas, Numpy, Plotly, Random <br>
Frameworks: Flask <br>
Web Technologies: HTML, CSS, Python

### Running the Scripts
For the user-side script, download the tiktok_custom directory and run:
```sh
python app.py
```
For the artist-side script, download the tiktok_artist directory and run:
```sh
python flask_backend.py
```

### Future Directions
Artist Dashboard Enhancements: Adding analytics like "User Base Interests" to show current genres and tracks favored by the artist's audience, guiding artists in their creative decisions.
Local Diversity Enhancements: Incorporating more features like artist names, spectral features, and language for user-side diversity recommendations.

### Closing Statement
Participating in this hackathon has been a remarkable experience. Initially, we doubted our ability to complete such a challenging project, but the past few days have demonstrated our potential to turn ideas into reality. We look forward to contributing more in the future and eagerly await similar challenges from TikTok.

