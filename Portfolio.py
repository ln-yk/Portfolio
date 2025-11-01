import streamlit as st
import pandas as pd
import time
import plotly.express as px
import base64

#                                     test lang ni dawg
# st.title("This is my porfolio")
# st.header("Welcome")
# st.write("This is my portfolio page where I showcase my projects and skills.")

# name = st.text_input("Enter your name:")
# if name:
#     st.write(f"Hello, {name}! Welcome to my portfolio.")

# number = st.slider("Enter your age: ", 0, 100)
# st.write(f"You are {number} years old.")

with open("citu.jpg", "rb") as f:    # open and read the image file para bg image sa sidebar
    img_base64 = base64.b64encode(f.read()).decode()

st.markdown(f"""    
<style>
[data-testid="stSidebar"] {{
    background-image: linear-gradient(rgba(128,0,0,0.54), rgba(0,0,0,0.85)), 
                      url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.9);
    color: white;

}}
</style>
""", unsafe_allow_html=True) # had to ask help from AI xDDDDDD


# PAGE SETUP
st.set_page_config(page_title="My Portfolio", page_icon="📘", layout="wide")

# HEADER SECTION
st.title("Portfolio")
st.markdown("### Welcome to my personal portfolio built with Streamlit")

# SIDEBAR NAVIGATION
st.sidebar.title("Suse's Portfolio")

page = st.sidebar.radio("Select Page", ["About Me", "Portfolio", "Skills", "Contact"])
st.sidebar.markdown("---")
st.sidebar.write("BS Computer Science - CIT-U")

# ABOUT ME PAGE
if page == "About Me":
    st.subheader("About Me")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("profile.jpg", width=150)
    with col2:
        st.subheader("Hi, I'm Aldrin Suse!")
        st.write("""
        I'm a computer science student currently studying in Cebu Institute of Technology - University who's interested in programming, data analysis, and game design.  
        
        I enjoy creating and designing user interfaces to enhance user experience by making applications
        visually appealing and efficient to navigate. In my free time, I like exploring AI models,
        improving my coding skills, and playing rhythm or story-based games.
        """)

    st.info("*Fun fact:* This guy has over 1500 achievements in genshin impact")

    with st.expander("My Computer Science Progression Timeline"):
        st.markdown("""
        - **2023:** Started coding and learning its fundamentals using C.
        - **2024:** Learned the basics of Web Development such as HTMl, CSS and JavaScript. Also started designing UI/UX using Canva and Figma.
        - **2024-2025:** Learned C++, Java, and Kotlin for Data Structures, Object-oriented Programming and Android Development.
        - **2025-Present:** Exploring AI, Data Visualization, Springboot, Django, and Image Processing using Python and C#.
        """)

# PORTFOLIO PAGE
elif page == "Portfolio":
    st.header("My Projects")
    st.markdown("Some personal projects that I've worked on:")

    tab1, tab2, tab3 = st.tabs(["📱 Web Apps", "🤖 AI Projects", "🎮 Games"])

    with tab1:
        st.subheader("Genshin-themed online vision store")

        st.write("""A fun little web app that features a timer on when the store opens, this was built for a practice on JavaScript.""")

        st.image("store1.png", caption="Image 1: Timer before store opens")
        st.image("store2.png", caption="Image 2: Items being sold in the store")

    with tab2:
        st.subheader("Neural Network Visualizer")
        st.write("Built a Python app that visualizes feedforward and backpropagation steps.")
        st.bar_chart([3, 6, 9, 12, 7, 6, 4])

    with tab3:
        st.subheader("FourLink (Connect 4 Game)")
        st.write("A two-player game built fully in Kotlin with a clean UI.")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("main_menu.png", caption="Main Menu")
        with col2:
            st.image("game_board.png", caption="Gameplay")
        with col3:
            st.image("game_over.png", caption="Win Screen")
        
    st.markdown("---")
    st.write("Here's a quick look at the number of projects completed per year:")

    df = pd.DataFrame({
        "Year": ["2023", "2024", "2025"],
        "Projects": [1, 5, 7]
    })
    chart = px.line(df, x="Year", y="Projects", title="Project Growth Over Time", markers=True)
    st.plotly_chart(chart, width='stretch')

# SKILLS PAGE
elif page == "Skills":
    st.header("My Skills")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Programming Languages")
        st.write("- Python 🐍")
        st.write("- C++ 💻")
        st.write("- Java ☕")
        st.write("- Kotlin 📱")
        st.write("- HTML/CSS/JS 🌐")
    with col2:
        st.subheader("Frameworks & Tools")
        st.write("- Django")
        st.write("- Streamlit")
        st.write("- Springboot")
        st.write("- Git & GitHub")

    st.markdown("### Skill Progress")
    st.write("A visual look at my current skill proficiency:")

    skills = {
        "Python": 30,
        "Java": 40,
        "C++": 70,
        "C": 60,
        "Kotlin": 20,
        "Data Visualization": 55
    }

    for skill, progress in skills.items():
        st.write(f"{skill} - {progress}%")
        st.progress(progress)

# CONTACT PAGE
elif page == "Contact":
    st.header("Contact Me")

    st.write("You can reach me through any of the following platforms:")

    col1, col2, col3 = st.columns(3)
    col1.link_button("GitHub", "https://github.com/ln-yk?tab=repositories", help="View my repositories", width='stretch')
    col2.link_button("Teams", "https://teams.microsoft.com/v2/", help="Aldrin D. Suse", width='stretch')
    col3.link_button("Email Me on Outlook", "mailto:aldrin.suse@cit.edu", width='stretch')

    st.markdown("---")
    st.subheader("Send me a Message")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    # just simulation, no actuial sending LOLOLOLOL
    if st.button("Send"):
        if name and email and message:
            with st.spinner("Sending message..."):
                time.sleep(1)
            st.success("Message sent!")
        else:
            st.warning("Please fill in all fields before sending.")

# FOOTER
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        © 2025 Aldrin Suse | Built with ♥ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

