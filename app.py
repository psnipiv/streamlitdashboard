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
    
    df_S1 = load_data_session("S1")
    df_S2 = load_data_session("S2")


    page = st.sidebar.selectbox("Choose a page", ['Home Page','Day 2 - Session 1', 'Day 2 - Session 2' ])

    if page == 'Home Page':
        st.title('Barcelona Test 2 Day 2')
        st.text('Select a page in the sidebar')

    elif page == 'Day 2 - Session 1':
        load_plot1(df_S1,0,50)
        load_heatmap(df_S1)
    elif page == 'Day 2 - Session 2':
        load_plot1(df_S2,0,160)
        load_heatmap(df_S2)
    else:
        st.text('Select a page in the sidebar')
        

@st.cache
def load_data_session(session):
    sessionfile = ''
    jsondata = '{}'
    if session == 'S1':
        sessionfile = 'Export_DataFrame_D2S1.json'
    elif session == 'S2':
        sessionfile = 'Export_DataFrame_D2S2.json'
        
    with open(sessionfile) as json_file:
        jsondata = json.load(json_file)
    data = pd.DataFrame(jsondata)
    return data

def load_plot1(df,startlap,endlap):
    fig = px.scatter(df, x="LAPS", y="S123", color="N",template="ggplot2",width=1200,height=600, hover_name="CURRENTLAP",trendline="lowess")
    fig.update_xaxes(range=[startlap,endlap],title_text='Lap Number')
    fig.update_yaxes(range=[77,102],title_text='Total sector time')
    st.plotly_chart(fig)

def load_heatmap(df):
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",marginal_x="box", trendline="ols")
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()