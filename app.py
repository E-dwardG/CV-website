import streamlit as st
from pathlib import Path
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Digital CV | Edward Gilbert", page_icon=":computer:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#load assets
local_css("styles/style.css")
lottie_animation = "https://lottie.host/e925d7f9-d7c3-49c7-bfcd-9faa560f419b/oLu1VR2VMb.json"
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "CV.pdf"
with open(resume_file, "rb") as pdf_file:
    PDFbyte_cv = pdf_file.read()
hackenbush_project_file = current_dir / "assets" / "Hackenbush_project.pdf"
with open(hackenbush_project_file, "rb") as pdf_file:
    PDFbyte_hackenbush_project = pdf_file.read()
profile_pic = current_dir / "assets" / "Pfp.png"
profile_pic = Image.open(profile_pic)

#Header
with st.container():
    L_col, R_col = st.columns((1, 3), gap="small")
    with R_col:
        st.title("Edward Gilbert - Mathematics Masters Graduate")
        st.write("#")
        inner_col1, inner_col2, inner_col3 = st.columns(3)
        with inner_col1:
            st.download_button(
                label="Download CV",
                data=PDFbyte_cv,
                file_name=resume_file.name,
                mime="application/octet-stream",
            )
        with inner_col2:
            st.write("[LinkedIn :necktie:](https://www.linkedin.com/in/edward-gilbert-maths/)")
        with inner_col3:
            st.write("[GitHub :computer:](https://github.com/E-dwardG)")
    with L_col:
        st.image(profile_pic, width=250)

with st.container():
    st.write("---")
    L_col, R_col = st.columns(2)
    with L_col:
        st.header("About me")
        st.write("##")
        st.write(
            """I am a conscientious fourth-year integrated Mathematics Master's student at the University of Warwick with key interests in combinatorics, graph theory, game theory as well as population and disease modelling. I have a strong desire to apply my strong mathematical modelling skills gained from the study of epidemiology to the world of financial markets or biotechnology."""
        )
    with R_col:
        st_lottie(lottie_animation, height=350, key="analysis")

with st.container():
    st.write("---")
    st.header("Achievements")
    #Hackenbush project
    L_col, M_col, R_col = st.columns((5, 1, 1), gap="small")
    with L_col:
        st.write(
            """
            - Wrote an essay on combinatorial game theory after having self-learnt the subject in second year. 
            The essay went into the surprising link between the games Nim and Hackenbush and how one can take some of the strategies used in the game Nim and transform them into strategies for Hackenbush.
            """
        )
    with M_col:
        st.download_button(
                label="Download Essay",
                data=PDFbyte_hackenbush_project,
                file_name=hackenbush_project_file.name,
                mime="application/octet-stream",
            )
    #HKO project
    L_col, M_col, R_col = st.columns((5, 1, 1), gap="small")
    with L_col:
        st.write(
            """
            - I created a project comparing the efficiency of the Hu-Kang-Othmer and the Gillespie algorithms for stochastic modelling, 
            using differing setups with varying amounts of rules and subrules. 
            This required creating various extreme models to really test the two methods, 
            showing that given enough rules and a clever subrule division, 
            the Hu-Kang-Othmer method will in fact start to become more efficient than Gillespie.
            """
        )
    with M_col:
        st.download_button(
                label="Placeholder",
                data=PDFbyte_hackenbush_project,
                file_name=hackenbush_project_file.name,
                mime="application/octet-stream",
            )
    with R_col:
        st.write("[Github Repository :computer:](https://github.com/E-dwardG/Gillespie-vs-HKO)")
    #Masters project
    L_col, M_col, R_col = st.columns((5, 1, 1), gap="small")
    with L_col:
        st.write(
            """
            - I developed stochastic models for exploring how varying different key parameters can affect the persistence of diseases collaborating with Professor Matt Keeling. 
            It involved use of diffusion approximations, as well as a deep understanding of stochastic processes.
            """
        )
    with M_col:
        st.download_button(
                label="Placeholder2",
                data=PDFbyte_hackenbush_project,
                file_name=hackenbush_project_file.name,
                mime="application/octet-stream",
            )
    with R_col:
        st.write("[Github Repository :computer:](https://github.com/E-dwardG/Disease-Persistence)")


#contact
with st.container():
    st.write("---")
    st.header("Email me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/edwardgilbert2002@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Name here" required>
     <input type="email" name="email" placeholder="Email address" required>
     <textarea name="message" placeholder="Message here" required></textarea>
     <button type="submit">Send</button>
    </form> 
    """

    L_col, R_col = st.columns(2)
    with L_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with R_col:
        st.empty()