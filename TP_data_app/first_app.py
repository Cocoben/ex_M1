import streamlit as st

#Librairies annexes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import os
rep_actuel = os.getcwd()

st.title('Petit TP data app')


@st.cache
def load_data_tv():
    data_tv = pd.read_csv(rep_actuel + "/data/tv_shows.csv")
    return data_tv

@st.cache
def load_data_movie():
    data_movie = pd.read_csv(rep_actuel + "/data/movie.csv")
    return data_movie


data_load_state = st.text('Chargement des données...')
data_tv = load_data_tv()
data_movie = load_data_movie()
data_load_state.text("Finis! (using st.cache)")

#Charger des jeux de données (au moins 2) présents dans votre répertoire local
#Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur

tab_selected = st.selectbox('Selectionnez un tableau :', ('Séries','Films'))
if tab_selected == 'Séries':
    tab_open = data_tv
else:
    tab_open = data_movie


st.subheader('Contenu')
number = st.number_input('Nombre de ligne : ')
number = int(number)
if st.checkbox('Afficher les ' + tab_selected):
    st.write(tab_open.head(number))

#Afficher le nom des colonnes du dataset
#Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées
#La shape du dataset, par lignes et par colonnes

st.subheader('Colonnes du tableau ' + tab_selected)
if st.checkbox('Afficher les colonnes'):
    st.markdown('Nom des colonnes')
    st.write(list(data_movie))
    st.markdown('Type des colonnes')
    st.write(data_movie.dtypes)
    st.markdown('Shape')
    st.write(data_movie.shape)
    st.markdown('Describe')
    st.write(data_movie.describe())


#st.pyplot(tab_open)
