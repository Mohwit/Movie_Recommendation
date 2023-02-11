import streamlit as st
import pickle
import requests

movies_df = pickle.load(open('movie.pkl', 'rb'))
movie_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=b25587cadc014bbcf38f0b9c3d577fb0".format(id))
    data = response.json()
    poster = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return  poster


# creating the function to recommend movie
def recommend(selected_movie, movies_df):
    index = movies_df[movies_df['title'] == selected_movie].index[0]
    distances = similarity[index]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for movi in movies:
        recommended_movies.append(movies_df.iloc[movi[0]].title)
        recommended_movies_poster.append(fetch_poster(movies_df.iloc[movi[0]].id))
    return recommended_movies , recommended_movies_poster


st.title('Movie Recommender System')
selected_movie = st.selectbox('Select your movie', movie_list)
if st.button('Recommend'):
    names, posters = recommend(selected_movie, movies_df)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader(names[0])
        st.image(posters[0])

    with col2:
        st.subheader(names[1])
        st.image(posters[1])

    with col3:
        st.subheader(names[2])
        st.image(posters[2])

    with col4:
        st.subheader(names[3])
        st.image(posters[3])

    with col5:
        st.subheader(names[4])
        st.image(posters[4])

