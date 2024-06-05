import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split, cross_validate
from collections import defaultdict
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import plotly.express as px

# Spotify API credentials
client_id = '246ca8283cee4b3396c38ad528466aa1'
client_secret = '6e2fec464e284c12b7ecbcadc3258ef3'

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to get album cover
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

# Load and preprocess demographics data
@st.cache_data
def load_and_preprocess_data():
    demographics = pd.read_csv('/Users/izzahalzahri/Desktop/P2/Dataset/demographics.csv')


# Load the new dataset
demographics = pd.read_csv('/Users/izzahalzahri/Desktop/P2/Dataset/demographics.csv')

# Display the first few rows of the dataset
st.write("## Demographic Data")
st.dataframe(data.head())

# Display distribution of ages
st.write("### Age Distribution")
fig_age = px.histogram(data, x='Age', title='Age Distribution')
st.plotly_chart(fig_age)

# Display gender distribution
st.write("### Gender Distribution")
fig_gender = px.pie(data, names='Gender', title='Gender Distribution')
st.plotly_chart(fig_gender)

# Display Spotify usage period distribution
st.write("### Spotify Usage Period")
fig_usage_period = px.histogram(data, x='spotify_usage_period', title='Spotify Usage Period')
st.plotly_chart(fig_usage_period)

# Display Spotify listening devices distribution
st.write("### Spotify Listening Devices")
fig_listening_device = px.bar(data, x='spotify_listening_device', title='Spotify Listening Devices')
st.plotly_chart(fig_listening_device)

# Display favorite music genres distribution
st.write("### Favorite Music Genres")
fig_music_genre = px.pie(data, names='fav_music_genre', title='Favorite Music Genres')
st.plotly_chart(fig_music_genre)

# Display preferred listening content distribution
st.write("### Preferred Listening Content")
fig_listening_content = px.bar(data, x='preferred_listening_content', title='Preferred Listening Content')
st.plotly_chart(fig_listening_content)

# Display music recommendation rating distribution
st.write("### Music Recommendation Rating")
fig_recc_rating = px.histogram(data, x='music_recc_rating', title='Music Recommendation Rating')
st.plotly_chart(fig_recc_rating)

# Display preferred podcast genres distribution
st.write("### Favorite Podcast Genres")
fig_podcast_genre = px.pie(data, names='fav_pod_genre', title='Favorite Podcast Genres')
st.plotly_chart(fig_podcast_genre)

# Display podcast listening frequency distribution
st.write("### Podcast Listening Frequency")
fig_podcast_frequency = px.histogram(data, x='pod_lis_frequency', title='Podcast Listening Frequency')
st.plotly_chart(fig_podcast_frequency)
