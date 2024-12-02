%%writefile Emofy_Enhancement.py
import numpy as np
import streamlit as st
from PIL import Image
from deepface import DeepFace
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
from streamlit_option_menu import option_menu

# Page icon
icon = Image.open("D:/All Documents/Final Year Project/FMBMRS Using DeepFace/Images/Logos/Emofy/LOGO1.png")

# Page configuration
st.set_page_config(
    page_title="EmoFy: A Facial Emotion Based Music Recommendation System",
    page_icon=icon,
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("<h2 style='text-align: center; color: #000080;'>Ramachandra College of Engineering</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #BDB76B;'>Department of Artificial Intelligence & Data Science</h2>", unsafe_allow_html=True)
st.text("")
st.text("")

# Page Styling
# Get the local file path for the background image
background_image_path = "D:/All Documents/Final Year Project/FMBMRS Using DeepFace/Images/Logos/Emofy/LOGO1.png"

# Page Styling with Background Image
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('{background_image_path}');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    .header-title {{
        font-size: 35px;
        font-weight: medium;
        color: #708090;
        text-align: left;
        margin-bottom: 30px;
    }}
    .emotion-text {{
        font-size: 24px;
        font-weight: bold;
        color: #4169e1;
        text-align: center;
        margin-bottom: 20px;
    }}
    .song-info {{
        font-size: 18px;
        color: #008080;
        text-align: center;
        margin-bottom: 20px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.balloons()


with st.sidebar:
    st.sidebar.image(icon, use_column_width=True)
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Project Details", "Contact"],
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
    )



# Home Section
if selected == "Home":
    # Spotify API credentials
    SPOTIPY_CLIENT_ID = 'c59262a9d28a4a06abc8c1f594f39a24'
    SPOTIPY_CLIENT_SECRET = '3391f3e4144b49418f6a38f55b4d3ce3'
    SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:000/callback'
    scope = "user-read-playback-state,user-modify-playback-state"

    # Function to play songs based on detected emotion
    def Play_Songs(detected_emotion, emotion_songs):
        try:
            # Initialize Spotify API client
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=SPOTIPY_CLIENT_ID,
                client_secret=SPOTIPY_CLIENT_SECRET,
                redirect_uri=SPOTIPY_REDIRECT_URI,
                scope=scope
            ))

            if detected_emotion in emotion_songs:
                emotion_dict = emotion_songs[detected_emotion]
                random_song_key = random.randint(1, 20)

                if random_song_key in emotion_dict:
                    song_name = emotion_dict[random_song_key]
                    st.markdown("<p class='song-info'>Now Playing: {}</p>".format(song_name), unsafe_allow_html=True)

                    # Search for the selected song using Spotify API
                    search_query = f"{song_name}"
                    results = sp.search(q=search_query, type="track", limit=1)
                    # Extract tracks from the search results
                    if results['tracks']['items']:
                        # Get all artists associated with the track                  
                        artists = [artist['name'] for artist in results['tracks']['items'][0]['artists']]

                        st.markdown("<p class='song-info'>Artists: {}</p>".format(", ".join(artists)), unsafe_allow_html=True)
                    
                        # Start playback with the selected song
                        sp.start_playback(uris=[results['tracks']['items'][0]['uri']])
                    else:
                        st.markdown("<p class='song-info'>No matching track found for song: {}</p>".format(song_name), unsafe_allow_html=True)
                else:
                    st.markdown("<p class='song-info'>Invalid song key for emotion: {}</p>".format(detected_emotion), unsafe_allow_html=True)
            else:
                st.markdown("<p class='song-info'>No songs found for emotion: {}</p>".format(detected_emotion), unsafe_allow_html=True)
        except spotipy.SpotifyException:
            st.markdown("<p class='song-info' style='color: red;'>Unable to Connect to Spotify: Please Activate The Device</p>", unsafe_allow_html=True)

    # Function to perform emotion detection
    def Emotion_Detection(image, emotion_songs):
        # Perform emotion analysis on the uploaded image
        Emo = DeepFace.analyze(image, actions="emotion", enforce_detection=False) 
        detected_emotion = Emo[0]["dominant_emotion"]
        st.markdown("<p class='emotion-text'>Dominant Emotion: {}</p>".format(detected_emotion), unsafe_allow_html=True)
        return Play_Songs(detected_emotion, emotion_songs)

    # Header
    st.markdown("<h1 class='header-title'>EmoFy: A Facial Emotion Based Music Recommendation System</h1>", unsafe_allow_html=True)
    # Header with college name and department name

    

    # Emotions along with related songs
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
            16: "JD Intro: Baground",
            17: "Killing Jeeja",
            18: "Vikram: Title Track",
            19: "Beast Mode",
            20: "The Revelation Interval BGM",
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
            11: "Chuttamalle",
            12: "Iraga Iraga",
            13: "Door Number Okati",
            14: "Oo Antava Oo Oo Antava",
            15: "Bujji Bangaram", 
            16: "Kalalo Kooda",
            17: "Gumma from ambajipeta marriage band",
            18: "Kammani",
            19: "Chinnadhana",
            20: "Gunde Jaari Gallanthayyinde",
        },
        "sad": {
            1: "Evaro Nenevaro",
            2: "Adiga Adiga",
            3: "Kanureppala Kaalam",
            4: "Adigaa from Hi Nanna",
            5: "Yedetthu Mallele",
            6: "Po Ve Po The Pain of Love",
            7: "Nee Navve",
            8: "Uppenantha",
            9: "O Manasa O Manasa",
            10: "Vrike Chilaka",
            11: "Heartbreak Anniversary",
            12: "Karige Loga",
            13: "Vinave Vinave from Raja Rani",
            14: "Nee Yadalo Naaku",
            15: "Athey Nanne",
            16: "Yaalo Yaalaa",
            17: "Sooreede from Salaar",
            18: "Vaalu Kanuladaanaa",
            19: "Gaaju Bomma",
            20: "Pilla Raa",
        },
        "neutral": {
            1: "Inka Edho",
            2: "Gilli Gilliga",
            3: "Em Sandeham Ledu from ",
            4: "Sirivennela",
            5: "Seethakaalam",
            6: "Langa  Voni",
            7: "Kopama Napina",
            8: "Neeve from Darling",
            9: "Sada Siva",
            10: "Idhe Kadha Nee Katha",
            11: "Cheppave Chirugali",
            12: "Choosa Choosa",
            13: "Buttabomma- Telugu",
            14: "Hoyna Hoyna from Gangu Leader",
            15: "Okey Oka Lokam",
            16: "Chilaka",
            17: "Potti Pilla",
            18: "Prema Ane",
            19: "Konchem Konchem",
            20: "Manasu Maree",
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
            12: "Pedda Puli from Chal Mohan Ranga",
            13: "Dandaalu Dandaalu",
            14: "Krishna Trance - From Karthikeya 2",
            15: "Jai Shri Ram Telugu ",
            16: "Mukundha Mukundha",
            17: "Raamam Raaghavam",
            18: "Sri Anjaneyam",
            19: "Shiva Shiva Shankara from Damarukam",
            20: "Hanuman Chalisa from HanuMan",
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
            12: "Konte Chooputho from Ananthapuram",
            13: "Mella Mellagaa",
            14: "Choodandi Saaru",
            15: "Urike Urike from HIT 2",
            16: "Anuvanuvuu",
            17: "Thattukolede",
            18: "Madam Sir Madam Anthe",
            19: "Suttamla Soosi",
            20: "Kutty Kudiye from Premalu",
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
            16: "Avunanavaa",
            17: "Inthandham",
            18: "Nagumomu Thaarale",
            19: "Arere Manasa from Falaknuma Das",
            20: "Oh Sita Hey Rama",
        },
    }

    # Ask user for option: upload image or use webcam
    
    option = st.radio("Choose An Option:", ("Upload Image", "Use Webcam"))

    # Upload image or capture image from webcam based on user's choice
    if option == "Upload Image":
        uploaded_image = st.file_uploader('Upload an image representing your current emotion')
        if uploaded_image:
            image = Image.open(uploaded_image)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            image = np.array(image)
            Emotion_Detection(image, emotion_songs)
            st.snow()
            
    elif option == "Use Webcam":
        uploaded_image = st.camera_input('Take an image representing your current emotion')
        if uploaded_image:
            image = Image.open(uploaded_image)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            image = np.array(image)
            Emotion_Detection(image, emotion_songs)
            st.snow()

elif selected == "Project Details":
     # Header
    st.markdown("<h2 class='sider-title' style='color: SlateGray ;'>Project Details</h2>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h3 class= 'sider-title' style='color:  ;'>Title:</h3>",unsafe_allow_html=True)
    st.write("")
    st.write("EmoFy: A Facial Emotion Based Music Recommendation System")
    st.markdown("<h3 class= 'sider-title' style='color: black;'>About EmoFy:</h3>",unsafe_allow_html=True)
    st.write("")
    st.write("EmoFy is an app that uses facial emotions to recommend personalized music playlists. By analyzing your real-time emotional state, EmoFy aims to enhance your listening experience and connect you to the perfect songs for your mood.")
    st.write("")
    st.write("It starts with capturing the image of yourself using the camera and then it sends it to the DeepFace model that is already pretrained. It analyzes the face you provided and then it gives you the exact emotion that your face is showing. It identifies emotions like happy, sad, anger, surprise, fear, neutral, and disgust. Once it understands your emotion, EmoFy then connects to the Spotify web using the Spotify auth method and then it plays a song that is mapped with the detected emotion.")
    st.write("")
    image="D:/All Documents/Final Year Project/FMBMRS Using DeepFace/Images/Logos/Emofy/LOGO1.png"
    image = Image.open(image)
    st.image(image, caption="EmoFy Logo", width=500, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
    
elif selected == "Contact":
    # Header
    st.markdown("<h2 class='sider-title' style='color: SlateGray;'>Project Team</h2>", unsafe_allow_html=True)
    st.text("")
    
    # Load and resize images
    nithin = Image.open("D:/All Documents/Final Year Project/FMBMRS Using DeepFace/Images/Nithin.jpg").resize((300, 300))
    sonia = Image.open("D:/All Documents/Final Year Project/FMBMRS Using DeepFace/Images/sony2.jpg").resize((300, 300))
    charmila = Image.open("D:/All Documents/Final Year Project/FMBMRS Using DeepFace/Images/Charmila.jpg").resize((300, 300))
    jithu = Image.open("D:/All Documents/Final Year Project/FMBMRS Using DeepFace/Images/Jithu2.jpg").resize((300, 300))

    # Team member details
    team_members = [
        {
            "name": "Nithin Reddy Ch",
            "Roll_Number": "20ME1A5409",
            "image": nithin
            
        },
        {
            "name": "Sonia Suvarna D",
            "Roll_Number": "20ME1A5415",
            "image": sonia
            
        },
        {
            "name": "Charmila M",
            "Roll_Number": "20ME1A5440",
            "image": charmila
            
        },
        {
            "name": "Jithendra Devi Prasad D",
            "Roll_Number": "20ME1A5418",
            "image": jithu
            
        }
    ]

    # Display team member details with images side by side
    col1, col2, col3, col4 = st.columns(4)

    for i, member in enumerate(team_members):
        with locals()[f"col{i+1}"]:
            st.image(member["image"], caption=member["name"], use_column_width=True)
            st.write(f"Name: {member['name']}")
            st.write(f"Roll Number: {member['Roll_Number']}")
