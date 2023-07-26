import streamlit as st
import pandas as pd
import numpy as np
import pickle


random_forest = pickle.load(open('Random_Forest_DayAhead.pkl', 'rb'))

class Day_ahead_prediction:
    def predict():
        st.write("Please enter the following data")
        with st.form("inputs"):
            col2, col3, col4 = st.columns(3)           
            with col2:
                lt24 = st.number_input(label="Load: 24 hours before", min_value=0.0, step = 1.0, value=1829.0)
                lt24 = (lt24-432)/(6306-432)
                lt48 = st.number_input(label="Load: 48 hours before", min_value=0.0, step=1.0, value=1967.0)
                lt48 = (lt48-432)/(6306-432)
                
            with col3:
                weekStatus = {"Sunday":1, "Weekday":0}
                week = st.selectbox("Day", weekStatus.keys())
                seasonStatus = {"Rainy": 0, "Winter": 1, "Summer": 2}
                season = st.selectbox("Season", seasonStatus.keys())

            with col4:
                temp = st.number_input("Temparature in Celcius", max_value=50.0, value=18.33, step=0.5, min_value=0.0)
                temp = (temp * 9/5) + 32
                humidity = st.number_input("Humidity %", min_value=25, max_value=100, value=92)
                humidity = (humidity-14)/(102-14)

            submitted = st.form_submit_button("Predict")

            if submitted:
                input = [lt24, lt48, weekStatus.get(week), seasonStatus.get(season)/2, (temp-50)/(108-50), humidity]
                random_forest_preds = random_forest.predict([input]) 
                res_random_forest = f"{random_forest_preds[0]*(6306-432)+432:.2f} KW"
                st.markdown(f"""
                #### The Estimated Load is: <span style = "color: green"> {res_random_forest} </span>
                """, unsafe_allow_html=True)
        


        fcol1, fcol2, fcol3, fcol4, fcol5 = st.columns(5)
        with fcol1:
            st.markdown("""
Project Members:   
- [Dr. Venkataramana Veeramsetty](https://www.linkedin.com/in/dr-venkataramana-veeramsetty-7a42871a4/)    
- [Modem Sai Pavan Kumar](https://www.linkedin.com/in/modem-sai-pavan-kumar-36a036223)   
- [Gudelli sushma vaishnavi](https://www.linkedin.com/in/sushma-vaishnavi-gudelli-390b60211)   
- [Potharaboina Prasanna](https://www.linkedin.com/mwlite/in/prasanna-potharaboina-a49853193)  
- [Nagula Sumanth](https://www.linkedin.com/in/sumanth-nagula-8a94a5104)   
- [Prabhu Kiran Konda](https://www.linkedin.com/in/prabhu-kiran-konda-b14619208/)
""")