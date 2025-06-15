📄 README.md – Projet Bank Marketing
Membre du groupe: Roa CHAIR, Sarah AMIAR, Bechir MEBARKI, Mohamed Amine GANNOUCHI
🎯 Objectif du Projet
Analyser une campagne marketing bancaire pour comprendre les facteurs influençant la souscription à une offre et prédire les clients susceptibles de souscrire, dans le but de mieux cibler les futures campagnes.

📁 Données utilisées
Fichier : bank.csv

Source : Kaggle - Bank Marketing Dataset

Nombre d’observations : 11 162

Colonnes clés :

age, job, marital, education : Profil client

contact, month, duration : Données de campagne

deposit : Variable cible (souscription oui/non)

🧰 Outils et bibliothèques
Python 3.x

Pandas, NumPy

Seaborn, Matplotlib

Scikit-learn (modélisation)

Streamlit (prévu pour dashboard interactif)

🔍 Étapes du projet
Chargement et nettoyage des données

Suppression des doublons

Encodage des variables catégorielles

Analyse exploratoire (EDA)

Visualisation des profils, taux de réponse, canaux de contact, etc.

Modélisation (Random Forest)

Classification binaire pour prédire deposit

Séparation train/test, entraînement et prédictions

Évaluation

Accuracy ~83%

Classification report : bon équilibre précision/rappel

Matrice de confusion analysée

Recommandations finales

Meilleur ciblage possible par métier, canal et période

Dashboard (à venir)

Interface interactive avec Streamlit (filtres + visualisations)

🚀 Comment exécuter le projet
bash
Copier
Modifier
pip install -r requirements.txt
jupyter notebook notebook.ipynb
📌 Résultats Clés
Le modèle atteint une accuracy de 83 %

Précision élevée sur les deux classes (souscription oui/non)

Variables influentes : duration, month, contact, job

Recommandations : optimiser les campagnes sur les canaux et périodes les plus performants