from deepface import DeepFace
import cv2
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import streamlit as st
import numpy as np
from PIL import Image





st.header('RCEE::AI&DS')
st.title('EMOFY APPLICATION')


emotion_songs = {
    "angry": {
        1: "My Love Is Gone",
        2: "Dhruva Dhruva from Dhruva",
        3: "The Monster Song",
        4: "Sainika",
        5: "Vilaya Pralaya Moorthy from Kanchana",
        6: "Salaam Rocky Bhai",
        7: "Salaar - Final Punch",
        8: "Sulthan from KGF 2",
        9: "Hukum - Thalaiver Alappara",
        10: "Rolex Theme - Background Score",
        11: "Dorikithe Chastavu",
        12: "Vangaveeti Katti",
        13: "Temper",
        14: "La La Bheemla",
        15: "Gola Petty",
    },
    "happy": {
        1: "Gudilo Badilo Madilo",
        2: "Humma Humma",
        3: "Poolamme Pilla",
        4: "Chamkeela Angeelesi",
        5: "One Two Three Four",
        6: "Neela Nilave from RDX",
        7: "Samajavaragamana",
        8: "Hamsaro",
        9: "Choopultho Guchi",
        10: "Hayyoda from Jawan",
        11: "Arere Yekkada",
        12: "Iraga Iraga",
        13: "Door Number Okati",
        14: "Oo Antava Oo Oo Antava",
        15: "Bujji Bangaram",       
    },
    "sad": {
        1: "Evaro Nenevaro",
        2: "Adiga Adiga",
        3: "Kanureppala Kaalam",
        4: "Adigaa from Hi Nanna",
        5: "Yedetthu Mallele",
        6: "Po Ve Po The Pain of Love",
        7: "Evarulerani",
        8: "Jabilli Kosam-Male",
        9: "O Manasa O Manasa",
        10: "Vrike Chilaka",
        11: "Heartbreak Anniversary",
        12: "Karige Loga",
        13: "Vinave Vinave",
        14: "Nee Yadalo Naaku",
        15: "Thalachi Thalachi",
    },
    "neutral": {
        1: "Inka Edho",
        2: "Gilli Gilliga",
        3: "Em Sandeham Ledu",
        4: "Sirivennela",
        5: "Seethakaalam",
        6: "Langa  Voni",
        7: "Kopama Napina",
        8: "Neeve from Darling",
        9: "Sada Siva",
        10: "Idhe Kadha Nee Katha",
        11: "Cheppave Chirugali",
        12: "Choosa Choosa",
        13: "Hello from Hello",
        14: "Hoyna Hoyna from Gangu Leader",
        15: "Maate Vinadhuga",
    },
    "fear": {
        1: "Stranger In Black Theme",
        2: "Vastunna Vachestunna",
        3: "Masss Theme",
        4: "Cheekatlo Kamme",
        5: "Bhayapadi Adivantha",
        6: "Agnimuni Bhagnamuni",
        7: "Nandikonda",
        8: "Varam Nan Unai",
        9: "Ninu Veedani Needanu Nene",
        10: "The Ghost",
        11: "Middle Of The Night",
        12: "Pedda Puli",
        13: "Dandaalu Dandaalu",
        14: "Krishna Trance - From Karthikeya 2",
        15: "Jai Shri Ram Telugu ",
    },
    "surprise": {
        1: "Ola Olaala Ala",
        2: "Kailove Chedugudu",
        3: "Kollagottey",
        4: "Baitikochi Chuste",
        5: "Jawan Title Track",
        6: "Idhazhin Oram - The Innocence of Love ",
        7: "Ordinary Person From Leo",
        8: "Adhento Ganni Vunnapaatuga Jersey",
        9: "Anaganaganaga",
        10: "Ee Raathale From Radhe Shyam",
        11: "Ninnila from Tholiprema",
        12: "Konte Chooputho",
        13: "Mella Mellagaa",
        14: "Choodandi Saaru",
        15: "Urike Urike from HIT 2",
    },
    "disgust": {
        1: "Mukundha Mukundha",
        2: "Arere Aakasham",
        3: "Reppakelaa Vodhaarpu",
        4: "Hrudayama From Major",
        5: "Sara Sari- Telugu",
        6: "Ee Manchullo",
        7: "Manasu Maree",
        8: "Nunugu Misalodu",
        9: "Chellamma From Doctor",
        10: "Chinnadana Neekosam",
        11: "Reppalanindaa",
        12: "Emannavoo",
        13: "Kaadhani Nuvvantunnadhi",
        14: "Inthalo Ennenni Vinthalo Male",
        15: "Champesaave Nannu",
    },
}

# Spotify API credentials
SPOTIPY_CLIENT_ID = '49d3fd6cddb14d2c9d8a27da18bc4210'
SPOTIPY_CLIENT_SECRET = '4bb6c9bd24324adb8dcd28dea37d4152'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:3000/callback'
scope = "user-read-playback-state,user-modify-playback-state"


image = st.file_uploader('Present your emotion')
if image:
    image=Image.open(image)
    st.image(image)
    image=np.array(image)
    # Analyzing image(face) using DeepFace.analyze 
    Millie_Emo = DeepFace.analyze(image, actions=['emotion'],enforce_detection=False )
    detected_emotion = Millie_Emo[0]["dominant_emotion"]
    st.text("Dominant Emotion:"+detected_emotion)
    # Emotions along with related songs


    # Initialize Spotify API client
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scope
    ))


    # Randomly Selecting Songs related to the detected emotion
    if detected_emotion in emotion_songs:
        emotion_dict = emotion_songs[detected_emotion]
        random_song_key = random.randint(1, 15)
    
        if random_song_key in emotion_dict:
            song_name = emotion_dict[random_song_key]
            print(f"Now Playing : {song_name}")

            # Search for the selected song using Spotify API
            search_query = f"{song_name}"
            results = sp.search(q=search_query, type="track", limit=1)

            # Extract tracks from the search results
            if results['tracks']['items']:
                # Get all artists associated with the track
                artists = [artist['name'] for artist in results['tracks']['items'][0]['artists']]
            
                st.text("Artists: "+str(artists))
            
                # Start playback with the selected song
                sp.start_playback(uris=[results['tracks']['items'][0]['uri']])
            else:
                st.text("No matching track found for song:"+song_name)
        else:
            st.text("Invalid song key for emotion:"+detected_emotion)
    else:
        st.text("No songs found for emotion:" +detected_emotion)
