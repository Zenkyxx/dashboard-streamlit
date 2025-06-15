
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuration de la page
st.set_page_config(page_title="Dashboard Marketing Bancaire", layout="wide")

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv("bank.csv")

df = load_data()

# Nettoyage
df.columns = df.columns.str.strip()
df['deposit'] = df['deposit'].map({'yes': 'oui', 'no': 'non'})

# Filtres
st.sidebar.header("🧰 Filtres")
selected_jobs = st.sidebar.multiselect("Profession", df['job'].unique(), default=df['job'].unique())
selected_edu = st.sidebar.multiselect("Education", df['education'].unique(), default=df['education'].unique())
selected_age = st.sidebar.slider("Âge", int(df['age'].min()), int(df['age'].max()), (20, 60))

filtered_df = df[
    (df['job'].isin(selected_jobs)) &
    (df['education'].isin(selected_edu)) &
    (df['age'].between(selected_age[0], selected_age[1]))
]

# Titre principal
st.markdown("## 📊 Dashboard Marketing Bancaire")

# Graphique 1 : Bar plot groupé par profession
fig1 = px.histogram(filtered_df, x="job", color="deposit", barmode="group",
                    title="Taux de souscription par profession")

# Graphique 2 : Boxplot - durée d'appel vs souscription
fig2 = px.box(filtered_df, x="deposit", y="duration", color="deposit",
              title="📞 Durée d’appel vs Souscription")

# Graphique 3 : Pie chart - répartition par éducation
edu_counts = filtered_df['education'].value_counts()
fig3 = px.pie(names=edu_counts.index, values=edu_counts.values,
              title="🎓 Répartition des clients par niveau d’éducation")

# Graphique 4 : Histogramme âge vs souscription
fig4 = px.histogram(filtered_df, x="age", color="deposit", barmode="overlay",
                    nbins=30, title="👤 Âge vs Souscription")

# Affichage en layout horizontal
col1, col2 = st.columns([3, 1])
with col1:
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.markdown("### 🎛️ Filtres")
    st.write("Profession sélectionnées :", ", ".join(selected_jobs))
    st.write("Niveaux d'éducation :", ", ".join(selected_edu))
    st.write(f"Tranche d'âge : {selected_age[0]} à {selected_age[1]} ans")

# Deuxième rangée de graphes
col3, col4, col5 = st.columns(3)
with col3:
    st.plotly_chart(fig2, use_container_width=True)
with col4:
    st.plotly_chart(fig3, use_container_width=True)
with col5:
    st.plotly_chart(fig4, use_container_width=True)
