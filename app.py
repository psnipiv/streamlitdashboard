import streamlit as st
import pandas as pd
import numpy as np
import json
import sys
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm


def main():

    df_r1M = load_data_session('r1M')
    df_r1P1 = load_data_session('r1P1')
    df_r1P2 = load_data_session('r1P2')
    df_r1P3 = load_data_session('r1P3')

    df_r2M = load_data_session('r2M')
    df_r2P1 = load_data_session('r2P1')
    df_r2P2 = load_data_session('r2P2')
    df_r2P3 = load_data_session('r2P3')


    page = st.sidebar.selectbox("Choose a page", ['Home Page','1-Austria GP','2-Styria GP' ])

    if page == 'Home Page':
        st.title('Formula 1 2020 Season')
        st.write("")
        st.write("Here is the interactive timing charts for lap times clocked by drivers of respective team during the Formula 1 2020 season.")
        st.write('')
        st.write("")
        st.text('Select a page in the sidebar')
        st.write("")
        st.write("Note : These charts are best to view in bigger screens")
        st.write("The interactive charts are created using plotly and the devlopment of user interface is done with streamlit nd deployed in heroku")

    elif page == '1-Austria GP':
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            sessionno = st.radio("Select Practice session",("Practice 1","Practice 2","Practice 3"))
            if sessionno =="Practice 1":
                if df_r1P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r1P1,0,50)
            elif sessionno =="Practice 2":
                if df_r1P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r1P2,0,55)
            elif sessionno =="Practice 3":
                if df_r1P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r1P3,0,25)
        elif testdayno == "Main Race":
            if df_r1M.empty:
                st.write("Session Data is not available.")
            else:
                st.write(df_r1M)
                load_plot2(df_r1M,1,75,60,130)
                load_plot3(df_r1M,1,75,60,80)
                load_plot4(df_r1M,1,75)
        else:
            st.write("Session Data is not available.")


    elif page == '2-Styria GP':
        # SelectBox
        testdayno = st.selectbox("Select Practice Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            sessionno = st.radio("Select session",("Practice 1","Practice 2","Practice 3"))
            if sessionno =="Practice 1":
                if df_r2P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r2P1,0,45)
            elif sessionno =="Practice 2":
                if df_r2P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r2P2,0,50)
            elif sessionno =="Practice 3":
                if df_r2P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r2P3,0,50)
        elif testdayno == "Main Race":
            if df_r2M.empty:
                st.write("Session Data is not available.")
            else:
                st.write(df_r2M)
                load_plot2(df_r2M,1,75,60,130)
                load_plot3(df_r2M,1,75,60,80)
                load_plot4(df_r2M,1,75)
        else:
            st.write("Session Data is not available.")
        
    else:
        st.text('Select a page in the sidebar')
        

@st.cache
def load_data_session(session):
    sessionfile = ''
    jsondata = '{}'
    if session == 'r1P1':
        sessionfile = '1-Final_Practice1Data.json'
    elif session == 'r1P2':
        sessionfile = '1-Final_Practice2Data.json'
    elif session == 'r1P3':
        sessionfile = '1-Final_Practice3Data.json'
    elif session == 'r1M':
        sessionfile = '1-Final_MainRaceData.json'

    elif session == 'r2P1':
        sessionfile = '2-Final_Practice1Data.json'
    elif session == 'r2P2':
        sessionfile = '2-Final_Practice2Data.json'
    elif session == 'r2P3':
        sessionfile = '2-Final_Practice3Data.json'
    elif session == 'r2M':
        sessionfile = '2-Final_MainRaceData.json'
        
    with open(sessionfile) as json_file:
        jsondata = json.load(json_file)
    data = pd.DataFrame(jsondata)
    return data

def load_plot1(df,startlap,endlap):
    fig = px.scatter(df, x="LAPS", y="S123", color="NAME",template="ggplot2",width=1200,height=600, hover_name="TYRE",trendline="lowess")
    fig.update_xaxes(range=[startlap,endlap],title_text='Lap Number')
    fig.update_yaxes(range=[60,150],title_text='Total sector time')
    st.plotly_chart(fig)

def load_plot2(df,startlap,endlap,mintime,maxtime):
    fig = px.scatter(df, x="LAPNO", y="S123", color="DRIVERCODE",template="ggplot2",width=1200,height=600, hover_name="TYRE",trendline="lowess")
    fig.update_xaxes(range=[startlap,endlap],title_text='Lap Number')
    fig.update_yaxes(range=[mintime,maxtime],title_text='Total sector time')
    st.plotly_chart(fig)

def load_plot3(df,startlap,endlap,mintime,maxtime):
    fig = px.scatter(df, x="LAPNO", y="S123", animation_frame="LAPNO", animation_group="NAME",size="S123", color="NAME", hover_name="CURRENTLAP", size_max=10,width=1200,height=600,range_y=[mintime,maxtime],range_x=[startlap,endlap])
    fig.update_xaxes(title_text='Lap Number')
    fig.update_yaxes(title_text='Total sector time')
    st.plotly_chart(fig)

def load_plot4(df,startlap,endlap):
    fig = px.scatter(df, x="LAPNO", y="P", animation_frame="LAPNO", animation_group="NAME",size="P", color="NAME", hover_name="CURRENTLAP", size_max=20,width=1200,height=600,range_y=[1,20],range_x=[startlap,endlap])
    fig.update_xaxes(title_text='Lap Number')
    fig.update_yaxes(title_text='Leader Board')
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()