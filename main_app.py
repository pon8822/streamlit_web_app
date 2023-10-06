import streamlit as st
from PIL import Image

st.title('アプリ')
st.caption('テストアプリです')

image = Image.open('./data/stable-diffusion-xl1.JPG')
st.image(image, width=200)
