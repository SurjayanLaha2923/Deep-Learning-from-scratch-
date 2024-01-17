# Import necessary libraries
import pandas as pd
import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load the pre-trained recommendation model
with open('spotify_millsongdata_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit app
st.title("Spotify Song Recommendation System")

# Get Spotify API credentials from Spotify Developer account
SPOTIPY_CLIENT_ID = '7a805b18766647f8809cd01d57acff26'
SPOTIPY_CLIENT_SECRET = '7c470252e9004e03b0782b976b77df2f'

# Set up Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

# User input for song
user_input = st.text_input("Enter a song name:", "Shape of You")

# Get song recommendations
if st.button("Get Recommendations"):
    # Get song details using Spotipy
    results = sp.search(q=user_input, type="track", limit=1)
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        track_name = results['tracks']['items'][0]['name']
        artist_name = results['tracks']['items'][0]['artists'][0]['name']
        st.write(f"Selected Song: {track_name} by {artist_name}")

        # Make recommendations using the pre-trained model
        recommendations = model.predict([track_id])
        recommended_songs = sp.tracks(recommendations)['tracks']

        # Display recommendations
        st.write("Recommended Songs:")
        for song in recommended_songs:
            st.write(f"{song['name']} by {song['artists'][0]['name']}")
    else:
        st.write("No results found for the given song.")

# To run the Streamlit app, save the code in a file (e.g., app.py) and run the following command in VS Code terminal:
# streamlit run app.py
