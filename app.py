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
            """I am a conscientious fourth-year integrated Mathematics Master's student at the University of Warwick with key interests in combinatorics, graph theory, game theory as well as population and disease modelling. I have a strong desire to apply my strong mathematical modelling skills gained from the study of epidemiology to the world of financial markets or insurance."""
        )
    with R_col:
        st_lottie(lottie_animation, height=350, key="analysis")

with st.container():
    st.write("---")
    L_col, R_col = st.columns((3, 2))
    with L_col:
        st.header("Technical skills")
        st.write("##")
        st.write(
            """
            - Strong scientific programming experience with: Python (numpy, scipy, pandas), Lean & R (ggplot2, dplyr) 
            - Strong software expertise with Linux & Github
            - Deep knowledge of: Stochastic modelling, Graph theory, Game theory, Discrete mathematics & algorithms
        """
        )
    with R_col:
        st.header("Soft skills")
        st.write("##")
        st.write(
            """
            - Confident presenter with years of radio and drama experience.
            - Organizational and project management skills gained from charity fundraisers, volunteering, and the leadership of university societies.

        """
        )

with st.container():
    st.write("---")
    st.header("Achievements")
    #Hackenbush project
    L_col, M_col, R_col = st.columns((5, 1, 1), gap="small")
    with L_col:
        st.write(
            """
            - I wrote an essay on combinatorial game theory after having self-learnt the subject in second year. 
            The essay showed links between two games and showed how strategies could be transferred between them. 
            This involved strategic thinking, problem solving and research.
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
            - I created a project comparing the efficiency of the Hu-Kang-Othmer and the Gillespie algorithms for stochastic modelling. 
            This involved stochastic modelling, setting up testing scenarios, as well as gathering and presenting data.
            """
        )

    #Masters project
    L_col, M_col, R_col = st.columns((5, 1, 1), gap="small")
    with L_col:
        st.write(
            """
            - I developed stochastic models for exploring how varying different key parameters can affect the persistence of diseases collaborating with Professor Matt Keeling. 
            It involved use of diffusion approximations, as well as a deep understanding of stochastic processes.
            """
        )
    
    st.write("Further resources will be posted here as my degree finishes and I am told I am allowed to do so.")

with st.container():
    st.write("---")
    L_col, R_col = st.columns(2)
    with L_col:
        st.header("Qualifications")
        st.write("Duke of Edinburgh silver award")
        st.write(
            """
            A-Levels:
            - Mathematics A*
            - Further Mathematics A*
            - Physics A*
            - Economics A*
        """
        )
        st.header("Employment history")
        st.write(
            """
        I have worked at a local arcade for Japanese multinational Bandai Namco for the past three summers. 
        This involved not just punctuality, reliability and flexibility, but also interactions with customers, 
        a highly demanding fast paced environment, as well as practical problem solving. 
        """
        )
    with R_col:
        st.header("Extracurricular activities")
        st.write(
            """
            - President for Warwick Offbeat society from March 2023 to March 2024: Involves organizing various events and making sure all aspects of the society from marketing to welfare are running smoothly and as a team. This helped build confidence and teamwork skills.
            - Presenter for Radio at Warwick from September 2022 to Present: Required me to be highly articulate, plan shows in advance, present on air, as well as manage problems when various technical issues have arisen.
            - Keen interest in the worlds of global economics, business and assets driven from taking various economics modules at university as well as consuming media and papers surrounding the subject.
            - Keen interest in technology, computer science and programming, encouraged by taking various modules on the subject, as well as having learnt a lot of discrete mathematics beyond university.

        """
        )

    
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