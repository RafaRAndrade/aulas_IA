import streamlit as st #Biblioteca para criar a interface web
import pandas as pd #Biblioteca para leitura e manipulação de dados
import json #Biblioteca para trabalhar com arquivos JSON

#Importa o vetorizador que transforma textos em valores numéricos
from sklearn.feature_extraction.text import TfidfVectorizer

#Importa o algoritmo de classificação supervisionada
from sklearn.linear_model import LogisticRegression

#Importa o Pipeline para organizar as etapas do modelo
from sklearn.pipeline import Pipeline