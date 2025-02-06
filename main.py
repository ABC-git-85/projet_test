import streamlit as st

# Définir les pages disponibles
pages = {
    "Site": [
        st.Page("pages/page1.py", title="Vols en live", icon="✈️"),
        st.Page("pages/page4.py", title="Statistiques de vols", icon="📈"),
    ],
}

pg = st.navigation(pages)
pg.run()