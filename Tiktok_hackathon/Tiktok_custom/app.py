from flask import Flask, request, render_template
import rl
app = Flask(__name__)
genres=[{'song': 'Arne Huseby - Warm Duck Shuffle', 'genre': 'Blues'}, {'song': 'Blind Boy Paxton - Mind Reader Blues (Live @ KEXP)', 'genre': 'Blues'}, {'song': 'Bombay Laughing Club - Workin Boy Blues', 'genre': 'Blues'}, {'song': 'Brother JT - Child of the Sun', 'genre': 'Blues'}, {'song': 'Brother JT - Hey Mr. Sun', 'genre': 'Blues'}, {'song': 'Brother JT - Interview', 'genre': 'Blues'}, {'song': 'Brother JT - Nothing Really', 'genre': 'Blues'}, {'song': 'Delta Dreambox - Queen of Loneliness', 'genre': 'Blues'}, {'song': 'F J Blues - The Message', 'genre': 'Blues'}, {'song': 'F J Blues - Unknown Man', 'genre': 'Blues'}, {'song': 'Ignatz - She Gets All That She Wants', 'genre': 'Blues'}, {'song': "Little Howlin' Wolf - Baltimore Raven", 'genre': 'Blues'}, {'song': "Little Howlin' Wolf - Blue Coochology", 'genre': 'Blues'}, {'song': 'Loren Connors and Bill Orcutt - Untitled 4', 'genre': 'Blues'}, {'song': "Nobody's Bizness - Come on in My Kitchen", 'genre': 'Blues'}, {'song': "Nobody's Bizness - Sittin' on Top of the World", 'genre': 'Blues'}, {'song': "Paul Wine Jones - Don't Laugh At Me", 'genre': 'Blues'}, {'song': 'Paul Wine Jones - If You Love Me Like You Say', 'genre': 'Blues'}, {'song': 'Paul Wine Jones - Nobody But You', 'genre': 'Blues'}, {'song': 'Paul Wine Jones - Pucker Up, Butter Cup', 'genre': 'Blues'}, {'song': 'Paul Wine Jones - Stop Arguing', 'genre': 'Blues'}, {'song': 'Roger McGuinn - 500 Miles', 'genre': 'Blues'}, {'song': 'Roger McGuinn - Joshua Fit the Battle of Jericho', 'genre': 'Blues'}, {'song': "T-Model Ford - Dust My Broom (live in the Kutsher's Country Club lobby)", 'genre': 'Blues'}, {'song': 'Wildbirds and Peacedrums - Doubt_Hope', 'genre': 'Blues'}, {'song': 'Wildbirds and Peacedrums - There Is No Light', 'genre': 'Blues'}, {'song': 'Achachak - 01 First Movement.mp3', 'genre': 'Classical'}, {'song': 'Achachak - Fifth Movement', 'genre': 'Classical'}, {'song': 'Achachak - First Movement', 'genre': 'Classical'}, {'song': 'Achachak - Fourth Movement', 'genre': 'Classical'}, {'song': 'Achachak - Second Movement', 'genre': 'Classical'}, {'song': 'Achachak - Third Movement (1)', 'genre': 'Classical'}, {'song': 'Achachak - Third Movement', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 01', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 02', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 03', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 04', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 05', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 07', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 08', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 10', 'genre': 'Classical'}, {'song': 'Megatone - Black and White 11', 'genre': 'Classical'}, {'song': 'Brakhage - 40th Mantra (Instrumental)', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - 40th Mantra', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - 41st Mantra (Bonus)', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - Le Vrai (Instrumental)', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - Le Vrai ft. Ibou', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - No Coincidence (Instrumental)', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - The Strike', 'genre': 'Hip-Hop'}, {'song': 'Brakhage - This Love (Instrumental)', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - Bad Trip', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - Delete', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - Endorphin Release', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - Nerves', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - Resident Evil', 'genre': 'Hip-Hop'}, {'song': 'Joint C Beat Laboratory - War with Yourself', 'genre': 'Hip-Hop'}, {'song': 'JsoundLAB - Soulful Calm Hip Hop', 'genre': 'Hip-Hop'}, {'song': '31 de Octubre - Milongueros', 'genre': 'Historic'}, {'song': 'Artur Aravidi - Rise (Epic, Inspirational, Cinematic)', 'genre': 'Historic'}, {'song': "Billy Murray - Are you the O'Reilly_", 'genre': 'Historic'}, {'song': 'Emin Efendi - Hale Makame', 'genre': 'Historic'}, {'song': 'Georgian State Folk Song and Dance Ensemble - Chakrulo', 'genre': 'Historic'}, {'song': 'Henry Burr - The girl from the U.S.A.', 'genre': 'Historic'}, {'song': 'Isidore Soucy - Quadrille Laurier (6ème Partie)', 'genre': 'Historic'}, {'song': 'Islam Yusufov - Song About Stalin', 'genre': 'Historic'}, {'song': 'J. O. LaMadeleine (& Jeannette) - Petite Lili Valse', 'genre': 'Historic'}, {'song': 'Jackson F. Smith - Cantina Rag', 'genre': 'Historic'}, {'song': 'John J. Kimmel - Medley of straight jigs', 'genre': 'Historic'}, {'song': 'Julio J. Martínez Oyanguren - Jota', 'genre': 'Historic'}, {'song': 'Levon Hampartzoumian - Menk Arghez Zinvor', 'genre': 'Historic'}, {'song': 'Parush Parushev - Nazko', 'genre': 'Historic'}, {'song': 'Performer not given. - [Piano solo--march]. (160 rpm)', 'genre': 'Historic'}, {'song': 'Polk Miller and his Old South Quartet - Jerusalem Mournin', 'genre': 'Historic'}, {'song': 'Rizeli Sadık - Erkek Kadın Oyun Havası', 'genre': 'Historic'}, {'song': 'Sam Castandet et son Orchestre Antillais - La Rue Zabyme', 'genre': 'Historic'}, {'song': "Seneca Indians - Children's Chorus", 'genre': 'Historic'}, {'song': 'Seneca Indians - Funeral Chant', 'genre': 'Historic'}, {'song': 'Septeto Machín - El Guateque', 'genre': 'Historic'}, {'song': 'Skarvelis, Kavouras, Peristeris - Pono, De Me Lypasai', 'genre': 'Historic'}, {'song': 'Stapleton Brothers - Call of the Whip-Poor-Will', 'genre': 'Historic'}, {'song': 'Tamburacı Osman Pehlivan - Anadolu Kaşık Havası', 'genre': 'Historic'}, {'song': 'Tefanake, Reia, and Moratai - Ute', 'genre': 'Historic'}, {'song': 'Will F. Denny - Uncle Harry, what is love_ (144 rpm)', 'genre': 'Historic'}, {'song': 'Zainab Palvanova - Ofarin', 'genre': 'Historic'}, {'song': 'Hawkin - Woods', 'genre': 'Instrumental'}, {'song': 'Horse Lords - Outer East', 'genre': 'Instrumental'}, {'song': 'Il Sogno Del Marinaio - Animal Farm Tango', 'genre': 'Instrumental'}, {'song': "Il Sogno Del Marinaio - Nanos' Waltz", 'genre': 'Instrumental'}, {'song': 'Il Sogno Del Marinaio - Partisian Song', 'genre': 'Instrumental'}, {'song': 'Il Sogno Del Marinaio - Verse IX', 'genre': 'Instrumental'}, {'song': 'Raul Diaz Palomar - Abdalá (demo, bonus)', 'genre': 'Instrumental'}, {'song': 'SalmonLikeTheFish - Glacier', 'genre': 'Instrumental'}, {'song': 'SalmonLikeTheFish - Sequoia', 'genre': 'Instrumental'}, {'song': 'SalmonLikeTheFish - Shenandoah', 'genre': 'Instrumental'}, {'song': 'SalmonLikeTheFish - Yellowstone', 'genre': 'Instrumental'}, {'song': 'SalmonLikeTheFish - Zion', 'genre': 'Instrumental'}, {'song': 'will austin - Reverie Solo Dec 2016a', 'genre': 'Instrumental'}, {'song': 'will austin - Reverie Solo Dec 2016b', 'genre': 'Instrumental'}, {'song': 'Dengue Fever - No Sudden Moves', 'genre': 'International'}, {'song': 'Dengue Fever - Sober Driver', 'genre': 'International'}, {'song': 'Judith Cohen - La muerte del Duque de Gandía', 'genre': 'International'}, {'song': 'Watcha Clan - Spanish Civil War Tribute', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - Boki Trinaest', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - Kozarica Kolo', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - Mig Mig', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - Prodzo Selo', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - [interview] (1)', 'genre': 'International'}, {'song': 'Zlatne Uste Balkan Brass Band - [interview]', 'genre': 'International'}, {'song': 'Ainst Char - Your Cellar, My Shrine', 'genre': 'Jazz'}, {'song': 'Albert Beger - Point of No Return', 'genre': 'Jazz'}, {'song': 'Albert Beger - Shasha', 'genre': 'Jazz'}, {'song': 'Barnacled - Polyurethane', 'genre': 'Jazz'}, {'song': 'Barnacled - Title', 'genre': 'Jazz'}, {'song': 'Breuss Arrizabalaga Quintet - Ghosts', 'genre': 'Jazz'}, {'song': 'Breuss Arrizabalaga Quintet - Pensamiento', 'genre': 'Jazz'}, {'song': 'Breuss Arrizabalaga Quintet - The Dark Side Of Frigiliana', 'genre': 'Jazz'}, {'song': 'HCI - partial autochthon', 'genre': 'Jazz'}, {'song': 'HCI - washing walls', 'genre': 'Jazz'}, {'song': 'Li Zenghui - soprano saxphone', 'genre': 'Jazz'}, {'song': 'Sid Peacock - Seagull choking on a ring pull', 'genre': 'Jazz'}, {'song': 'Sid Peacock - Want', 'genre': 'Jazz'}, {'song': 'Till Paradiso - Friends will be Friends (TP 70)', 'genre': 'Jazz'}, {'song': 'Till Paradiso - New Ideas (TP 76)', 'genre': 'Jazz'}, {'song': 'Here Comes A Big Black Cloud!! - Black Mold', 'genre': 'Rock'}, {'song': 'Here Comes A Big Black Cloud!! - Death March', 'genre': 'Rock'}, {'song': 'Here Comes A Big Black Cloud!! - The Fly Pt. II', 'genre': 'Rock'}, {'song': 'Matte Black - Loch', 'genre': 'Rock'}, {'song': 'Matte Black - Lungs', 'genre': 'Rock'}, {'song': 'Rod - Inner Guitars', 'genre': 'Rock'}, {'song': 'Rod - Sursaut', 'genre': 'Rock'}, {'song': 'The New Lines - Please Fall In Love', 'genre': 'Rock'}, {'song': 'The New Lines - Sentry On Patrol', 'genre': 'Rock'}, {'song': 'The New Lines - Year Of The Nines', 'genre': 'Rock'}]
temp=['Blues','Hip-Hop','International','Rock','Historic','Jazz','Classical','Instrumental']
p=[]
opt_2=[]
opt_1=[]
@app.route('/')
def index():
    global p, opt_1,opt_2
    options = get_initial_options()
    p=options[1]
    opt_1= options[0]
    opt_2=options[2]
    return render_template('index.html', options=options[0])

@app.route('/submit', methods=['POST'])
def submit():
    global p,opt_1,opt_2
    selected_option = request.form.get('option')
    R,top_n_items,genre_recommend,all_songs,threshold,genre_user= p
    
    # Process the selected option here and generate new options
    new_options = generate_new_options(selected_option,R,top_n_items,genre_user,all_songs,threshold,genre_recommend)
    p = new_options[1]
    opt_1=new_options[0]
    opt_2=new_options[2]
    
    return render_template('index.html', options=new_options[0])

def get_initial_options():
    R,top_n_items,genre_recommend,all_songs,threshold,genre_user=rl.recommendation()
    print(threshold,'threshold')
    print(f"\nTop 4 recommendations for user {0}: {top_n_items}")

    print(genre_recommend)
    print("Songs", [all_songs[i] for i in top_n_items])
    print("Song belongs to genre\n")
    for i in top_n_items:
        print(genres[all_songs[i]]['genre'])
    # Initial set of options
    return [[
        str(genres[all_songs[top_n_items[0]]]['song'])+' Genre '+str(genres[all_songs[top_n_items[0]]]['genre']),
        str(genres[all_songs[top_n_items[1]]]['song'])+' Genre '+str(genres[all_songs[top_n_items[1]]]['genre']),
        str(genres[all_songs[top_n_items[2]]]['song'])+' Genre '+str(genres[all_songs[top_n_items[2]]]['genre']),
        str(genres[all_songs[top_n_items[3]]]['song'])+' Genre '+str(genres[all_songs[top_n_items[3]]]['genre']),
    ],[R,top_n_items,genre_recommend,all_songs,threshold,genre_user],[[
       all_songs[top_n_items[0]],
       all_songs[top_n_items[1]],
       all_songs[top_n_items[2]]],
       all_songs[top_n_items[3]], 
    ]]

def generate_new_options(selected_option,R,top_n_items,genre_user,all_songs,threshold,genre_recommend):
    # Placeholder function to generate new options based on the selected option
    global opt_1,opt_2
    name_index=opt_1.index(selected_option)
    song_id= top_n_items[name_index]
    R,top_n_items,genre_recommend,all_songs,threshold,genre_user=rl.call_recommendation_again(R,top_n_items,genre_user,all_songs,threshold,genre_recommend,song_id)

    # return [
    #     f"New Option 1 after {selected_option}",
    #     f"New Option 2 after {selected_option}",
    #     f"New Option 3 after {selected_option}",
    #     f"New Option 4 after {selected_option}",
    #     f"New Option 5 after {selected_option}"
    # ]
    return [[
        str(genres[all_songs[top_n_items[0]]]['song'])+' Genre '+str(genres[all_songs[top_n_items[0]]]['genre']),
        str(genres[all_songs[top_n_items[1]]]['song'])+' Genre '+str(genres[all_songs[top_n_items[1]]]['genre']),
        str(genres[all_songs[top_n_items[2]]]['song'])+' Genre '+str(genres[all_songs[top_n_items[2]]]['genre']),
        str(genres[all_songs[top_n_items[3]]]['song'])+' Genre '+str(genres[all_songs[top_n_items[3]]]['genre']),
    ],[R,top_n_items,genre_recommend,all_songs,threshold,genre_user],[[
       all_songs[top_n_items[0]],
       all_songs[top_n_items[1]],
       all_songs[top_n_items[2]]],
       all_songs[top_n_items[3]], 
    ]]
if __name__ == '__main__':
    app.run(debug=True)
