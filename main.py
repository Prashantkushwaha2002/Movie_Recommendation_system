import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('MOVIE RECOMMENDER SYSTEM')

selected_movie_name = st.selectbox(
    'Which movie you would like to be recommended by?',
    movies['title'].values
)

if st .button('recommend'):
    recommended_movie_names= recommend(selected_movie_name)
    for movies in recommended_movie_names :
        st.write(movies)







