from pathlib import Path

import streamlit as st 
from PIL import Image


# Configuration des paths
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
cvPdf = current_dir / "assets" / "CvTwings.pdf"
photoProfil = current_dir / "assets" / "photoProfil.png"
photoProjet1 = Image.open("assets/tictactoe.png")
photoProjet2 = Image.open("assets/sudoku.png")





# --- DESCRIPTION GENERAL ---
PAGE_TITLE = "CV | Twingstan Edward"
PAGE_ICON = ":wave:"
NAME = "Twingstan Edward"
DESCRIPTION = """
Un finissant en multimédia qui s'intéresse au monde de la technologie, et passionné par la programmation. 
Je suis à la recherche  d'un stage dans le domaine du jeux vidéo ou dans le web. 
J’aime concevoir des modèles 3D. 
"""

SOCIAL_MEDIA_ICONS = {
    "LinkedIn": "assets/icons/linkedin.png",
    "GitHub": "assets/icons/github.png",
    "Behance": "assets/icons/behance.png",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- charger le CSS, PDF et les images ---
#photo de profil
photoProfil = Image.open(photoProfil)
#css
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
#pdf    
with open(cvPdf, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    


#SECTION INTRO
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(photoProfil, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')


#LES RESEAUX SOCIAUX
col5, col6, col7 = st.columns(3)
with col5:
    st.markdown('<div style="display: flex; justify-content: center;"><a href="https://github.com/twings07"><img src="https://img.icons8.com/ffffff/github"/></a></div>', unsafe_allow_html=True)
with col6:
    st.markdown('<div style="display: flex; justify-content: center;"><a href="https://www.linkedin.com/in/edward-twingstan"><img src="https://img.icons8.com/ffffff/linkedin.png"/></a></div>', unsafe_allow_html=True)
with col7:
    st.markdown('<div style="display: flex; justify-content: center;"><a href="https://www.behance.net/twingsEdward"><img src="https://img.icons8.com/ffffff/behance"/></a></div>', unsafe_allow_html=True)
st.write('\n')
st.write('\n')


# --- COMPETENCES---
st.write("----")
st.write('\n')
st.subheader("Compétences")
col3, col4 = st.columns(2, gap="small")
with col3:
    st.write(
        """
    <div class="vertical-list">
        <div class="hover-content">
            <span class="title"> <p> ✔️ Conception de sites Web </p> </span>
            <div class="details">
                <p> • HTML </p>
                <p> • CSS </p>
                <p> • SQL </p>
                <p> • PHP </p>
            </div>
        </div>
         <div class="hover-content">
            <span class="title"> <p> ✔️ Édition vidéo </p> </span>
            <div class="details">
                <p>• Premiere Pro</p>
                <p>• After Effects</p>
            </div>
        </div>
         <div class="hover-content">
            <span class="title"> <p> ✔️ Montages vidéo </p> </span>
            <div class="details">
                <p>• Premiere Pro</p>
                <p>• After Effects</p>
            </div>
        </div>
         <div class="hover-content">
            <span class="title"> <p> ✔️ Suite Adobe </p> </span>
            <div class="details">
                <p>• Premiere Pro</p>
                <p>• After Effects</p>
                <p>• Photoshop</p>
                <p>• Lightroom</p>
                <p>• XD</p>
                <p>• Encoder</p>
            </div>
        </div>
    </div>    
        """
        ,
        unsafe_allow_html=True
    )

with col4:
     st.write(
        """
    <div class="vertical-list">
        <div class="hover-content">
            <span class="title"> <p> ✔️ Conception de Jeux vidéo </p> </span>
            <div class="details">
                <p> • c# </p>
                <p> • Javascript</p>
                <p> • Python </p>
                <p> • Unity </p>
            </div>
        </div>
         <div class="hover-content">
            <span class="title"> <p> ✔️ Conception de modèles 3D </p> </span>
            <div class="details">
                <p> • Maya 3D</p>
                 <p> • Mudbox</p>
            </div>
        </div>
         <div class="hover-content">
            <span class="title"> <p> ✔️ Conception d’animations </p> </span>
            <div class="details">
                <p> • Illustrator </p>
                <p> • Photoshop </p>
                <p> • Unity </p>
            </div>
        </div>
         <div class="hover-content">
            <span class="title"> <p> ✔️ Suite Autodesk </p> </span>
            <div class="details">
                <p> • Maya 3D</p>
                 <p> • Mudbox</p>
            </div>
        </div>
        <div class="hover-content">
            <span class="title"> <p> ✔️ Unity </p> </span>
            <div class="details">
                <p> • c#</p>
                <p> • Unity 3D </p>
                <p> • Unity 2D </p>
            </div>
        </div>
        
    </div>    
        """
        ,
        unsafe_allow_html=True
    )

# --- EXPERIENCES PROFESSIONNELLES ---
st.write('\n')
st.write("----")
st.subheader("Expériences professionnelles")
st.write(
    """
-   2018 - 2023 Salle de réception Eveagreen:
    -   Serveur
    -   Livreur
-   2018 - 2024 Winners:
    -   Associé de magasin
    -   Caissier
"""
)

# --- FORMATIONS ---
st.write('\n')
st.write("----")
st.subheader("Formations")
st.write(
    """
-  2019 - 2024 D.E.C Intégration multimédia
-  2014 - 2019 D.E.S 
"""
)


# --- PROJETS ---
st.write('\n')
with st.container():
    st.write("----")
    st.subheader("Mes projets")
    st.write("##")
    image_column, description_column = st.columns((1, 2))
    with image_column:
        st.image(photoProjet1)
    with description_column:
        st.subheader("TicTacToe")
        st.write(
            """
            J'ai développé un jeu de Tic Tac Toe personnalisé en utilisant Python et Pygame, 
            où les joueurs utilisent deux images adorables de chats comme symboles. 
            """
        )
        st.markdown("[GitHub](https://github.com/twings07/TicTacToe)", unsafe_allow_html=True)
        
        
    
    st.write("##")
    image_column, description_column = st.columns((1, 2))
    with image_column:
        st.image(photoProjet2)
    with description_column:
        st.subheader("Sudoku")
        st.write(
            """
           J'ai développé un jeu de Sudoku en utilisant Python avec l'aide de Pygame et de la bibliothèque Dokusan, qui présente un défi classique de Sudoku.
            Le jeu utilise un algorithme de backtracking pour résoudre les planches de Sudoku.
            """
        )
        st.markdown("[GitHub](https://github.com/twings07/Sudoku)", unsafe_allow_html=True)
    
    
    #Section pour sidebar    
    st.sidebar.title("Retrouvez-moi ici")
    st.sidebar.write(""" 
             Vous trouverez ci-dessous tous les moyens de me contacter, ainsi que mes profils sur les réseaux sociaux. 
             Explorez mes liens pour en apprendre davantage sur mes projets et mon parcours professionnel.
             """)
    st.sidebar.markdown('<a href="https://github.com/twings07"><img src="https://img.icons8.com/ffffff/28/github"/> Github </a>', unsafe_allow_html=True)
    st.sidebar.markdown('<a href="https://www.linkedin.com/in/edward-twingstan"><img src="https://img.icons8.com/ffffff/28/linkedin.png"/> LinkedIn </a>', unsafe_allow_html=True)        
    st.sidebar.markdown('<a href="https://www.behance.net/twingsEdward"><img src="https://img.icons8.com/ffffff/28/behance"/> Behance </a>', unsafe_allow_html=True)
    st.sidebar.write("Mon CV est disponible ici.")
    st.sidebar.download_button(
        label=" 📄 CV ",
        data=PDFbyte,
        file_name=cvPdf.name,
        mime="application/octet-stream",
    )   