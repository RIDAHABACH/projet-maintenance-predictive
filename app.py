import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Chargement du modèle entraîné
model = joblib.load("models/random_forest_model.pkl")

# Titre et description de l’application
st.title("Maintenance Predictive - Tesla Framework")
st.markdown("Prediction de la duree de vie restante (RUL) d'un moteur turbofan")

# Upload du CSV
uploaded_file = st.file_uploader(
    "Importer un fichier CSV contenant les donnees moteur",
    type=["csv"]
)

if uploaded_file:
    # Lecture du CSV dans un DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Affichage rapide des 5 premieres lignes
    st.subheader("Apercu des donnees")
    st.dataframe(df.head())

    # Verification des colonnes necessaires
    required_columns = ['temperature', 'vibration', 'pressure', 'efficiency']
    if all(col in df.columns for col in required_columns):
        X = df[required_columns]        # Extraction des features
        predictions = model.predict(X)  # Prediction de la RUL
        df["RUL_predite"] = predictions  # Ajout de la colonne resultat

        # Affichage du tableau final (features + prediction)
        st.subheader("Resultats de la prediction")
        st.dataframe(df[required_columns + ["RUL_predite"]].head())

        # Visualisation de la distribution des predictions
        st.subheader("Visualisation des predictions")
        fig, ax = plt.subplots()
        ax.hist(predictions, bins=30, edgecolor='black')
        ax.set_title("Distribution des RUL predits")
        ax.set_xlabel("RUL (cycles)")
        ax.set_ylabel("Frequence")
        st.pyplot(fig)

        # Message de succes
        st.success("Predictions terminees")
    else:
        # Message d'erreur si colonnes manquantes
        st.error(
            f"Le fichier doit contenir les colonnes : {', '.join(required_columns)}"
        )
