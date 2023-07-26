import re
import streamlit as st
# import streamlit.components.v1 as components
import json
import requests
import streamlit as st

def about():
    st.markdown("""
<font size = '5'> This web application is useful to forecast the active power load on a 33/11KV substation which is located at Godishala (Village), Saidapur (Mandal), Karimnagar, Telangana State, India. This application forecast the load at particular time of the day based on load available in previous two hours, load available at same time but previous two days, status of the day, status of the season, temperature and humidity. Three machine learning models i.e. linear regression, decision tree and random forest are trained and tested for the load forecasting. Mean Square Error (MSE) on testing data for models i.e., linear regression, decision tree and random forest are 0.00513,0.00523 and 0.003835 respectively. This web application is developed using random forest model as this model predicting the load with less error i.e.  0.003835.</font>
    
| Machine Learning Model | MSE      |
| ---------------------- | -------- |
| Linear Regression      | 0.00513  |
| Decision Tree          | 0.00523  |
| Random Forest          | 0.003835 |
    """, unsafe_allow_html=True)