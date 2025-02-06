import streamlit as st

# Définir les pages disponibles
pages = {
    "Site": [
        st.Page("pages/page1.py", title="Vols en live", icon="✈️"),
        st.Page("pages/page2.py", title="Statistiques de vols", icon="📈"),
        st.Page("pages/page3.py", title="Prix des vols", icon="💺"),      
    ],
    "Ressources": [
        st.Page("pages/source.py", title="Nos sources", icon="📘"),
        st.Page("pages/equipe.py", title="À propos de nous", icon="ℹ️")
    ],
}

pg = st.navigation(pages)
pg.run()