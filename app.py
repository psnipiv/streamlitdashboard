import streamlit as st
import pandas as pd
import numpy as np
import json
import sys
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


COLOR = "black"
BACKGROUND_COLOR = "#fff"


def main():
    load_pages()
    select_block_container_style()



def load_pages():
    # Race 1 Data
    df_r1M = load_data_session('r1M')
    df_r1P1 = load_data_session('r1P1')
    df_r1P2 = load_data_session('r1P2')
    df_r1P3 = load_data_session('r1P3')
    # Race 2 Data
    df_r2M = load_data_session('r2M')
    df_r2P1 = load_data_session('r2P1')
    df_r2P2 = load_data_session('r2P2')
    df_r2P3 = load_data_session('r2P3')
    # Race 3 Data
    df_r3M = load_data_session('r3M')
    df_r3P1 = load_data_session('r3P1')
    df_r3P2 = load_data_session('r3P2')
    df_r3P3 = load_data_session('r3P3')
    # Race 4 Data
    df_r4M = load_data_session('r4M')
    df_r4P1 = load_data_session('r4P1')
    df_r4P2 = load_data_session('r4P2')
    df_r4P3 = load_data_session('r4P3')


    page = st.sidebar.selectbox("Choose a page", ['Home Page','1-Austria GP','2-Styria GP','3-Hungary GP', '4-British GP' ])

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
                    load_plot1(df_r1P1,0,50,60,150)
                    load_plot4(df_r1P1,60,150)

            elif sessionno =="Practice 2":
                if df_r1P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r1P2,0,55,60,150)
                    load_plot4(df_r1P2,60,150)
            elif sessionno =="Practice 3":
                if df_r1P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r1P3,0,25,60,150)
                    load_plot4(df_r1P3,60,150)
        elif testdayno == "Main Race":
            if df_r1M.empty:
                st.write("Session Data is not available.")
            else:
                st.write(df_r1M.describe())                
                load_plot2(df_r1M,1,75,60,130)
                load_plot3(df_r1M,65,71)
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
                    load_plot1(df_r2P1,0,45,60,150)
                    load_plot4(df_r2P1,60,150)
            elif sessionno =="Practice 2":
                if df_r2P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r2P2,0,50,60,150)
                    load_plot4(df_r2P2,60,150)
            elif sessionno =="Practice 3":
                if df_r2P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r2P3,0,50,60,150)
                    load_plot4(df_r2P3,60,150)
        elif testdayno == "Main Race":
            if df_r2M.empty:
                st.write("Session Data is not available.")
            else:
                st.write(df_r2M.describe())
                load_plot2(df_r2M,1,75,60,130)
                load_plot3(df_r2M,65,71)
        else:
            st.write("Session Data is not available.")


    elif page == '3-Hungary GP':
        # SelectBox
        testdayno = st.selectbox("Select Practice Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            sessionno = st.radio("Select session",("Practice 1","Practice 2","Practice 3"))
            if sessionno =="Practice 1":
                if df_r3P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r3P1,0,40,70,160)
                    load_plot4(df_r3P1,70,170)
            elif sessionno =="Practice 2":
                if df_r3P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r3P2,0,20,70,160)
                    load_plot4(df_r3P2,70,170)
            elif sessionno =="Practice 3":
                if df_r3P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r3P3,0,30,70,160)
                    load_plot4(df_r3P3,70,170)
        elif testdayno == "Main Race":
            if df_r3M.empty:
                st.write("Session Data is not available.")
            else:
                st.write(df_r3M.describe())
                load_plot2(df_r3M,1,75,60,140)
                load_plot3(df_r3M,75,85)
        else:
            st.write("Session Data is not available.")


    elif page == '4-British GP':
        # SelectBox
        testdayno = st.selectbox("Select Practice Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            sessionno = st.radio("Select session",("Practice 1","Practice 2","Practice 3"))
            if sessionno =="Practice 1":
                if df_r4P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r4P1,0,30,80,180)
                    load_plot4(df_r4P1,80,180)
            elif sessionno =="Practice 2":
                if df_r4P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r4P2,0,30,80,180)
                    load_plot4(df_r4P2,80,180)
            elif sessionno =="Practice 3":
                if df_r4P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plot1(df_r4P3,0,30,80,180)
                    load_plot4(df_r4P3,80,180)
        elif testdayno == "Main Race":
            if df_r4M.empty:
                st.write("Session Data is not available.")
            else:
                st.write(df_r4M.describe())
                load_plot2(df_r4M,1,75,60,140)
                load_plot3(df_r4M,75,85)
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

    elif session == 'r3P1':
        sessionfile = '3-Final_Practice1Data.json'
    elif session == 'r3P2':
        sessionfile = '3-Final_Practice2Data.json'
    elif session == 'r3P3':
        sessionfile = '3-Final_Practice3Data.json'
    elif session == 'r3M':
        sessionfile = '3-Final_MainRaceData.json'

    elif session == 'r4P1':
        sessionfile = '4-Final_Practice1Data.json'
    elif session == 'r4P2':
        sessionfile = '4-Final_Practice2Data.json'
    elif session == 'r4P3':
        sessionfile = '4-Final_Practice3Data.json'
    elif session == 'r4M':
        sessionfile = '4-Final_MainRaceData.json'
        
    with open(sessionfile) as json_file:
        jsondata = json.load(json_file)
    data = pd.DataFrame(jsondata)
    return data

def load_plot1(df,startlap,endlap,mintime,maxtime):
    df = df.sort_values(['N'],ascending=[1])
    fig = px.scatter(df, x="LAPS", y="S123", color="NAME",template="ggplot2",width=1200,height=600, hover_name="TYRE",trendline="lowess")
    fig.update_xaxes(range=[startlap,endlap],title_text='Lap Number')
    fig.update_yaxes(range=[mintime,maxtime],title_text='Total sector time')
    st.plotly_chart(fig)

def load_plot2(df,startlap,endlap,mintime,maxtime):
    df = df.sort_values(['N'],ascending=[1])
    fig = px.scatter(df, x="LAPNO", y="S123", color="DRIVERCODE",template="ggplot2",width=1200,height=600, hover_name="TYRE",trendline="lowess")
    fig.update_xaxes(range=[startlap,endlap],title_text='Lap Number')
    fig.update_yaxes(range=[mintime,maxtime],title_text='Total sector time')
    st.plotly_chart(fig)

def load_plot3(df,mintime,maxtime):
    df = df.sort_values(['N'],ascending=[1])
    sns.set(style="darkgrid")
    st.text('Heatmap')
    dataset = df.pivot("LAPNO", "DRIVERCODE", "S123")
    f, ax = plt.subplots(figsize=(25, 25))
    sns.heatmap(dataset, annot=True, cmap="cubehelix",vmin=mintime, vmax=maxtime, linewidths=0.5, fmt='g')
    sns.despine(left=True, bottom=True)
    st.pyplot()

def load_plot4(df,mintime,maxtime):
    df = df.sort_values(['N'],ascending=[1])
    optiontyres = st.radio("By Tyre or Overall?",("Tyre Category","Overall"))
    if optiontyres =="Tyre Category":
        fig = px.box(df, x="NAME", y="S123",color="TYRE",width=1200,height=600)
    elif optiontyres == "Overall":
        fig = px.box(df, x="NAME", y="S123",color ="NAME",width=1200,height=600)
    fig.update_yaxes(range=[mintime,maxtime],title_text='Total sector time')
    st.plotly_chart(fig)



def select_block_container_style():
    """Add selection section for setting setting the max-width and padding
    of the main block container"""

    max_width_100_percent = st.sidebar.checkbox("Set max width to 100%", False)
    if not max_width_100_percent:
        max_width = 1400
    else:
        max_width = 2000
    padding_top = 5
    padding_right = 1
    padding_left = 1
    padding_bottom = 10


    _set_block_container_style(
        max_width,
        max_width_100_percent,
        padding_top,
        padding_right,
        padding_left,
        padding_bottom,
    )


def _set_block_container_style(max_width: int = 1200,max_width_100_percent: bool = False,padding_top: int = 5,padding_right: int = 1,padding_left: int = 1,padding_bottom: int = 10):
    if max_width_100_percent:
        max_width_str = f"max-width: 100%;"
    else:
        max_width_str = f"max-width: {max_width}px;"
    st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        {max_width_str}
        padding-top: {padding_top}rem;
        padding-right: {padding_right}rem;
        padding-left: {padding_left}rem;
        padding-bottom: {padding_bottom}rem;
    }}
    .reportview-container .main {{
        color: {COLOR};
        background-color: {BACKGROUND_COLOR};
    }}
</style>
""",
        unsafe_allow_html=True,
    )




if __name__ == '__main__':
    main()