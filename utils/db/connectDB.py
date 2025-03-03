import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = st.secrets["URI_URL"]
client = MongoClient(uri, server_api=ServerApi("1"))
db = client["valentine_rec_sys"]
collection = db["responses"]


def connectDB():
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
