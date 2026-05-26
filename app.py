import streamlit as st
import pickle

movies_list = pickle.load(open('movies.pkl','rb'))
movies = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies_list[movies_list['title']==movie].index[0]
    distances = similarity[movie_index]
    recommended_movies = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    for i in recommended_movies:
        st.write(movies_list.iloc[i[0]].title)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Search your movie',
    movies
)

if st.button('Recommend'):
    recommend(selected_movie_name)
    