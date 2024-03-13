from pathlib import Path

import streamlit as st 
from PIL import Image


# Configuration des paths
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
cvPdf = current_dir / "assets" / "CvTwings.pdf"
photoProfil = current_dir / "assets" / "photoProfil.png"

# --- DESCRIPTION GENERAL ---
PAGE_TITLE = "CV | Twingstan Edward"
PAGE_ICON = ":wave:"
NAME = "Twingstan Edward"
DESCRIPTION = """
Un finissant en multimédia qui s'intéresse au monde de la technologie, et passionné par la programmation. 
Je suis à la recherche  d'un stage dans le domaine du jeux vidéo ou dans le web. 
J’aime concevoir des modèles 3D. 
"""
EMAIL = "twingstan2503@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/edward-twingstan",
    "GitHub": "https://https://github.com/twings07",
    "Behance" : "https://www.behance.net/twingsEdward",
}
PROJECTS = {
    "🏆 ",
    "🏆 ",
    "🏆 ",
    "🏆 ",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF et l'image ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(cvPdf, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
photoProfil = Image.open(photoProfil)

# --- Header ---
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(photoProfil, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 CV ",
        data=PDFbyte,
        file_name=cvPdf.name,
        mime="application/octet-stream",
    )
    

# --- Liens pour les reseaux sociaux ---
    
    st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA)) # len sert a compter le nmb de colonne dans "social_media"
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f'<a href="{link}" class="social-link">{platform}</a>',
        unsafe_allow_html=True)



# --- Compétences---
st.subheader("Compétences")

col3, col4 = st.columns(2, gap="small")

with col3: st.write(
    """
-  Web & Multimédia 
    -  Conception de sites Web
    -  Édition vidéo
    -  Montages vidéo
    -  Suite Adobe
    -  HTML, CSS, SASS, PHP, SQL
"""
)
with col4: st.write(
    """
-   Animation et Jeux
    -  Conception de Jeux vidéo
    -  Conception de modèles 3D
    -  Conception d’animations
    -  Suite Autodesk
    -  Unity
    -  c#, Javascript, Python
"""
)

# --- Éducation---
st.write('\n')
st.subheader("Éducation")
st.write(
    """
-  2019 - 2024 D.E.C Intégration multimédia
-  2014 - 2019 D.E.S 
"""
)

# --- Expériences professionnelles---
st.write('\n')
st.subheader("Expériences professionnelles")
st.write(
    """
-   2018 - 2023 Salle de réception Eveagreen:
    -   Serveur
    -   Livreur
-   2018 - 2023 Winners:
    -   Associé de magasin
    -   Caissier
"""
)


