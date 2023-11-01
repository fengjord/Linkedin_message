import langchain_helper as lch
import streamlit as st
import os

st.title("Linkedin Message Generator")

myname = st.sidebar.text_area (label="What is your name",max_chars=25)
name = st.sidebar.text_area (label="What is the name of the person you are looking to connect with?",max_chars=25)
position = st.sidebar.text_area(label="What position is this person?", max_chars = 30)
company = st.sidebar.text_area(label="What company is he/she working in?", max_chars = 20)
connection = st.sidebar.selectbox("What connection is this?",("1st connection", "2nd connection", "3rd+ connection"))
button = st.button(label="Submit", type="primary")

if button:
    response = lch.generate_linkedin_message(connection = connection, myname = myname, name=name, position = position, company = company)
    st.text(response['linkedin_message'])
