import streamlit as st 
from utils.db.connectDB import connectDB 
from utils.getEmbedding import getEmbedding
from utils.getMatch import getMatch

st.title("Valentine Recommendation System")

st.divider()

st.write("Fill the questions to get a match")

st.image("https://images.squarespace-cdn.com/content/v1/5b9580a050a54f9cd774077b/1607548759310-R91WKR9QPXMA85PFPF42/kawaii.png")

favorite_snacks = st.text_input("Waht is your favorite snack?")
favorite_programming_language = st.text_input("What is your favorite programming language?")
favorite_editor = st.text_input("What is your favorite code editor?")
favorite_browser = st.text_input("What is your favorite browser to use?")
favorite_breakfast = st.text_input("What is your go-to breakfast?")
favorite_show = st.text_input("What is your favorite show?")

if st.button("Submit"):
    st.success("Match has been found!")
else:
    st.warning("Please fill all of the questions")


connectDB()
getEmbedding()
getMatch()
