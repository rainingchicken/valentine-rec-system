import streamlit as st
from utils.db.connectDB import connectDB
from utils.db.postResponse import postResponse
from utils.getEmbedding import getEmbedding
from utils.getMatch import getMatch

st.title("Valentine Recommendation System")

st.divider()

st.write("Fill the questions to get a match")

st.image(
    "https://images.squarespace-cdn.com/content/v1/5b9580a050a54f9cd774077b/1607548759310-R91WKR9QPXMA85PFPF42/kawaii.png"
)

name = st.text_input("Waht is your name")
favorite_snacks = st.text_input("Waht is your favorite snack?")
favorite_programming_language = st.text_input(
    "What is your favorite programming language?"
)
favorite_editor = st.text_input("What is your favorite code editor?")
favorite_browser = st.text_input("What is your favorite browser to use?")
favorite_breakfast = st.text_input("What is your go-to breakfast?")
favorite_show = st.text_input("What is your favorite show?")

connectDB()

if st.button("Submit"):
    if (
        name 
        and favorite_snacks
        and favorite_programming_language
        and favorite_editor
        and favorite_browser
        and favorite_breakfast
        and favorite_show
    ):
        responses = {
            name: name,
            favorite_snacks: favorite_snacks,
            favorite_programming_language: favorite_programming_language,
            favorite_editor: favorite_editor,
            favorite_browser: favorite_browser,
            favorite_breakfast: favorite_breakfast,
            favorite_show: favorite_show,
        }
        responses_text = " ".join(responses.values())
        current_embedding = getEmbedding(responses_text)
        current_user_id = postResponse(responses, current_embedding)
        match = getMatch(current_embedding, current_user_id)

        if match:
            top_match_similarity, top_match_responses = match[0]
            result = ' '
            result = result.join(match[0][1])
            st.success(f"Match found! Here's someone similar to you: {result}")
            st.write(f"Similarity score: {top_match_similarity}")
        else:
            st.warning("No matches found. Be the first to enter the system!")
    else:
        st.warning("Please fill all of the question blanks")


