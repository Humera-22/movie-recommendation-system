import streamlit as st
import pickle
import pandas as pd
import requests
import time
import os


def fetch_poster(movie_id):
    """Fetch movie poster safely from TMDB, retry once if connection fails."""

    API_KEY = os.getenv("TMDB_API_KEY")   # ✅ added (ONLY change)

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    for attempt in range(2):  # try twice at most
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get("poster_path")

            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            else:
                return "https://via.placeholder.com/500x750?text=No+Poster"

        except requests.exceptions.ConnectionError as e:
            print(f"⚠️ Connection failed for {movie_id}, retrying... ({attempt+1}/2)")
            time.sleep(1)  # wait a bit before retry
        except Exception as e:
            print(f"⚠️ Error fetching poster for {movie_id}: {e}")
            break  # stop retrying for other types of errors

    # fallback image if both attempts fail
    return "https://via.placeholder.com/500x750?text=Error"


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        time.sleep(0.5)  # prevent hitting API too fast
    return recommended_movies, recommended_movies_posters


# Load data
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies["title"].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    #  Cleaner output using a loop
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            st.image(posters[i], use_container_width=True)

