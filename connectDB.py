import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri_url = st.secrets["URI_URL"]
client = MongoClient(uri_url, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)