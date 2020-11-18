import streamlit as st

#Librairies annexes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import os
rep_actuel = os.getcwd()

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('TP Série Film')


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
if st.button('Afficher les colonnes'):
    st.write(list(tab_open))
if st.button('Type des colonnes'):
    st.write(tab_open.dtypes)
if st.button('Afficher shape'):
    st.text('Nombre de lignes')
    st.write(tab_open.shape[0])
    st.text('Nombre de colonnes')
    st.write(tab_open.shape[1])
    st.text('Shape global')
    st.write(tab_open.shape)
if st.button('Afficher Describe'):
    st.markdown('Describe')
    st.write(tab_open.describe())


#st.write(sns.lineplot(tab_open['Year'] ))

tab_open['Year'] = pd.to_datetime(tab_open['Year'])
#st.bar_chart(tab_open['Netflix','Disney+'])


#displot



#Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)
#st.write(sns.heatmap(tab_open.corr(),annot=True))


#Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis)
if st.checkbox('Sortie des '+tab_selected+' par années'):
    st.write(sns.displot(tab_open.Year, bins=20, kde=False, aspect= 3))
    st.pyplot()


if st.checkbox('Répartition des platformes'):
    st.write(plt.pie(platforme, autopct = "%.2f"))
    st.pyplot()

dico = {
    'Netflix':[tab_open['Netflix'].sum()],
    'Disney+':[tab_open['Disney+'].sum()],
    'Hulu':[tab_open['Hulu'].sum()],
    'Prime Video':[tab_open['Prime Video'].sum()]
}
platforme = pd.DataFrame(dico)

st.write(platforme)

