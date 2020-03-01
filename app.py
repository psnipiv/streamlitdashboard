import streamlit as st
import pandas as pd
import numpy as np
import json
import sys
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import plotly.express as px
import statsmodels.api as sm


def main():
    df_d1S1 = load_data_session('d1S1')
    df_d1S2 = load_data_session('d1S2')
    df_d2S1 = load_data_session('d2S1')
    df_d2S2 = load_data_session('d2S2')
    df_d3S1 = load_data_session('d3S1')
    df_d3S2 = load_data_session('d3S2')


    page = st.sidebar.selectbox("Choose a page", ['Home Page','F1 Testing 2' ])

    if page == 'Home Page':
        st.title('Barcelona Test 2')
        st.text('Select a page in the sidebar')
        st.write("Here is the interactive timing charts for lap times clocked by drivers of respective team during the Formula 1 Test 2 2020 at Barcelona. However, there are many unknowns in the testing and details of tyres and sprints were not completely provided by FIA. Let's wait for couple of weeks to find the fastest car.")
        st.write('')
        st.write("")
        st.write("Note : These charts are best to view in bigger screens")
        st.write("The interactive charts are created using plotly and the devlopment of user interface is done with streamlit nd deployed in heroku")




    elif page == 'F1 Testing 2':
        # SelectBox
        testdayno = st.selectbox("Select Day",["Day 1","Day 2","Day 3"])
        st.write("On ", testdayno)

        if testdayno == "Day 1":
            sessionno = st.radio("Select session",("Morning","Afternoon"))
            if sessionno =="Morning":
                load_plot1(df_d1S1,0,90)
            elif sessionno =="Afternoon":
                load_plot1(df_d1S2,0,120)
        elif testdayno == "Day 2":
            sessionno = st.radio("Select session",("Morning","Afternoon"))
            if sessionno =="Morning":
                load_plot1(df_d2S1,0,50)
            elif sessionno =="Afternoon":
                load_plot1(df_d2S2,0,160)
        elif testdayno == "Day 3":
            sessionno = st.radio("Select session",("Morning","Afternoon"))
            if sessionno =="Morning":
                load_plot1(df_d3S1,0,90)
            elif sessionno =="Afternoon":
                load_plot1(df_d3S2,0,190)
        
    else:
        st.text('Select a page in the sidebar')
        

@st.cache
def load_data_session(session):
    sessionfile = ''
    jsondata = '{}'
    if session == 'd1S1':
        sessionfile = 'Export_DataFrame_D1S1.json'
    elif session == 'd1S2':
        sessionfile = 'Export_DataFrame_D1S2.json'
    elif session == 'd2S1':
        sessionfile = 'Export_DataFrame_D2S1.json'
    elif session == 'd2S2':
        sessionfile = 'Export_DataFrame_D2S2.json'
    elif session == 'd3S1':
        sessionfile = 'Export_DataFrame_D3S1.json'
    elif session == 'd3S2':
        sessionfile = 'Export_DataFrame_D3S2.json'
        
    with open(sessionfile) as json_file:
        jsondata = json.load(json_file)
    data = pd.DataFrame(jsondata)
    return data

def load_plot1(df,startlap,endlap):
    fig = px.scatter(df, x="LAPS", y="S123", color="N",template="ggplot2",width=1200,height=600, hover_name="CURRENTLAP",trendline="lowess")
    fig.update_xaxes(range=[startlap,endlap],title_text='Lap Number')
    fig.update_yaxes(range=[75,175],title_text='Total sector time')
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()