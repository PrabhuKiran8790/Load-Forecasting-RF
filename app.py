import base64
from pathlib import Path
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from predict import *
from about import *
from DALF import *

st.set_page_config(page_title='Load Forecasting', page_icon='⚡', layout="wide", initial_sidebar_state="expanded", menu_items=None)

icol1, icol2, icol3 = st.columns([1,6,1])
with icol1:
    st.write("")
with icol2:
    banner = st.image(Image.open('transco.jpeg'), use_column_width='auto', output_format='png')
with icol3:
    st.write("")

st.markdown("""
<div style="text-align:center"><h4>Electric Power Load Prediction on a 33/11 KV Substation
<p>(Godishala, Saidapur, Telangana, India)</p></div>
""", unsafe_allow_html=True)


app_logo = st.sidebar.image(Image.open('electricity-psd.png'), width=75,)

choice = st.sidebar.selectbox("Select an option", ("Hour Ahead Forecasting","Day Ahead Forecasting","About"))

if choice == 'Hour Ahead Forecasting':
    Prediction.predict()
if choice == 'About':
    about()
if choice == 'Day Ahead Forecasting':
    Day_ahead_prediction.predict()

st.sidebar.markdown("#")
st.sidebar.markdown("#")
st.sidebar.markdown("#")
st.sidebar.markdown("#")
st.sidebar.markdown("#")
st.sidebar.markdown("#")
# st.sidebar.markdown("#")
# st.sidebar.markdown("#")
st.sidebar.markdown("#####")
st.sidebar.markdown("#####")
st.sidebar.markdown("#####")
st.sidebar.markdown("#####")
st.sidebar.markdown("#####")
st.sidebar.markdown("#####")
st.sidebar.markdown("#####")
st.sidebar.markdown("######")
st.sidebar.markdown("######")

st.sidebar.markdown('---')

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

header_html = '<img src="data:image/png;base64,{}" class="img-fluid" width="300" height="170">'.format(
    img_to_bytes("logos.png")
    )
st.sidebar.markdown(
    header_html, unsafe_allow_html=True,
)
# logo = st.sidebar.image(Image.open('logos.png'), use_column_width='auto')

# st.markdown("""
# Project Members:   
# - [Dr. Venkataramana Veeramsetty](https://www.linkedin.com/in/dr-venkataramana-veeramsetty-7a42871a4/)    
# - [Modem Sai Pavan Kumar](https://www.linkedin.com/in/modem-sai-pavan-kumar-36a036223)   
# - [Gudelli sushma vaishnavi](https://www.linkedin.com/in/sushma-vaishnavi-gudelli-390b60211)   
# - [Potharaboina Prasanna](https://www.linkedin.com/mwlite/in/prasanna-potharaboina-a49853193)  
# - [Nagula Sumanth](https://www.linkedin.com/in/sumanth-nagula-8a94a5104)   
# - [Prabhu Kiran Konda](https://www.linkedin.com/in/prabhu-kiran-konda-b14619208/)
# """)

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            #MainMenu {visibility: hidden;
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
st.markdown(hide_img_fs, unsafe_allow_html=True)
