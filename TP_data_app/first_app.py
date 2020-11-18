import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import os
rep_actuel = os.getcwd()

st.title('Petit TP data app')


@st.cache
def load_data_tv(nrows):
    data_tv = pd.read_csv(rep_actuel + "/data/tv_shows.csv",nrows=nrows)
    return data_tv

@st.cache
def load_data_movie(nrows):
    data_movie = pd.read_csv(rep_actuel + "/data/movie.csv",nrows=nrows)
    return data_movie


data_load_state = st.text('Chargement des données...')
data_tv = load_data_tv(10000)
data_movie = load_data_movie(10000)
data_load_state.text("Finis! (using st.cache)")

st.subheader('Série')
if st.checkbox('Afficher les séries'):
    st.subheader('Série TV')
    st.write(data_tv)


st.subheader('Film')
number = st.number_input('Nombre de ligne : ')
number = int(number)
if st.checkbox('Afficher les filmes'):
    st.subheader('Film')
    st.write(data_movie.head(number))


dfVgSales.columns.tolist()

list(data)