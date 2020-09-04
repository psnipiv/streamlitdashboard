import streamlit as st
import pandas as pd
import numpy as np
import json
import sys
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import math


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
    # Race 5 Data
    df_r5M = load_data_session('r5M')
    df_r5P1 = load_data_session('r5P1')
    df_r5P2 = load_data_session('r5P2')
    df_r5P3 = load_data_session('r5P3')
    # Race 6 Data
    df_r6M = load_data_session('r6M')
    df_r6P1 = load_data_session('r6P1')
    df_r6P2 = load_data_session('r6P2')
    df_r6P3 = load_data_session('r6P3')
    # Race 7 Data
    df_r7M = load_data_session('r7M')
    df_r7P1 = load_data_session('r7P1')
    df_r7P2 = load_data_session('r7P2')
    df_r7P3 = load_data_session('r7P3')
    # Race 7 Data
    df_r8M = load_data_session('r8M')
    df_r8P1 = load_data_session('r8P1')
    df_r8P2 = load_data_session('r8P2')
    df_r8P3 = load_data_session('r8P3')
    
    page = st.sidebar.selectbox("Choose a page", ['Home Page','1-Austria GP','2-Styria GP','3-Hungary GP', '4-British GP', "5-70th Anniversary GP", "6-Spanish GP","7-Belgium GP","8-Italian GP" ])

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
                    load_plots(df_r1P1,True)
            elif sessionno =="Practice 2":
                if df_r1P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r1P2,True)
            elif sessionno =="Practice 3":
                if df_r1P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r1P3,True)
        elif testdayno == "Main Race":
            if df_r1M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r1M.describe())                
                load_plot2(df_r1M,1,75,60,130)
                load_plot3(df_r1M,65,71)
        else:
            st.write("Session Data is not available.")


    elif page == '2-Styria GP':
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            sessionno = st.radio("Select Practice Session",("Practice 1","Practice 2","Practice 3"))
            if sessionno =="Practice 1":
                if df_r2P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r2P1,True)
            elif sessionno =="Practice 2":
                if df_r2P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r2P2,True)
            elif sessionno =="Practice 3":
                if df_r2P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r2P3,True)
        elif testdayno == "Main Race":
            if df_r2M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r2M.describe())
                load_plot2(df_r2M,1,75,60,130)
                load_plot3(df_r2M,65,71)
        else:
            st.write("Session Data is not available.")


    elif page == '3-Hungary GP':
        # SelectBox
        testdayno = st.selectbox("Select Practice Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            sessionno = st.radio("Select Practice Session",("Practice 1","Practice 2","Practice 3"))
            if sessionno =="Practice 1":
                if df_r3P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r3P1,True)
            elif sessionno =="Practice 2":
                if df_r3P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r3P2,True)
            elif sessionno =="Practice 3":
                if df_r3P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r3P3,True)
        elif testdayno == "Main Race":
            if df_r3M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r3M.describe())
                load_plot2(df_r3M,1,75,60,140)
                load_plot3(df_r3M,75,85)
        else:
            st.write("Session Data is not available.")


    elif page == '4-British GP':
        # SelectBox
        testdayno = st.selectbox("Select Session",["Practice","Main Race"])
        st.write("On ", testdayno)

        if testdayno == "Practice":
            sessionno = st.radio("Select Practice Session",("Practice 1","Practice 2","Practice 3"))
            if sessionno =="Practice 1":
                if df_r4P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r4P1,True)
            elif sessionno =="Practice 2":
                if df_r4P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r4P2,True)
            elif sessionno =="Practice 3":
                if df_r4P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r4P3,True)
        elif testdayno == "Main Race":
            if df_r4M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r4M.describe())
                load_plot2(df_r4M,1,55,85,170)
                load_plot3(df_r4M,85,105)
        else:
            st.write("Session Data is not available.")


    elif page == '5-70th Anniversary GP':
        st.markdown("""# Formula 1 - 70th Anniversary Grand Prix 2020""")
        # SelectBox
        testdayno = st.selectbox("Select  Session",["Practice","Main Race"])

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("5-Practice.md"))
            sessionno = st.radio("Select Practice Session",("Practice 1","Practice 2","Practice 3"))
            if sessionno =="Practice 1":
                if df_r5P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r5P1,True)
            elif sessionno =="Practice 2":
                if df_r5P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r5P2,True)
            elif sessionno =="Practice 3":
                if df_r5P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r5P3,True)
        elif testdayno == "Main Race":
            if df_r5M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r5M.describe())
                load_plot2(df_r5M,1,55,85,125)
                load_plot3(df_r5M,85,105)
        else:
            st.write("Session Data is not available.")


    elif page == '6-Spanish GP':
        st.markdown("""# Formula 1 - Spanish GP 2020""")
        # SelectBox
        testdayno = st.selectbox("Select  Session",["Practice","Main Race"])

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("6-Practice.md"))
            sessionno = st.radio("Select Practice Session",("Practice 1","Practice 2","Practice 3"))
            if sessionno =="Practice 1":
                if df_r6P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r6P1,True)
            elif sessionno =="Practice 2":
                if df_r6P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r6P2,True)
            elif sessionno =="Practice 3":
                if df_r6P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r6P3,True)
        elif testdayno == "Main Race":
            if df_r6M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r6M.describe())
                load_plot2(df_r6M,1,66,55,110)
                load_plot3(df_r6M,80,95)
        else:
            st.write("Session Data is not available.")


    elif page == '7-Belgium GP':
        st.markdown("""# Formula 1 - Belgium GP 2020""")
        # SelectBox
        testdayno = st.selectbox("Select  Session",["Practice","Main Race"])

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("7-Practice.md"))
            sessionno = st.radio("Select Practice Session",("Practice 1","Practice 2","Practice 3"))
            if sessionno =="Practice 1":
                if df_r7P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r7P1,True)
            elif sessionno =="Practice 2":
                if df_r7P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r7P2,True)
            elif sessionno =="Practice 3":
                if df_r7P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r7P3,True)
        elif testdayno == "Main Race":
            if df_r7M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r7M.describe())
                load_plot2(df_r7M,1,44,75,190)
                load_plot3(df_r7M,105,125)
        else:
            st.write("Session Data is not available.")


    elif page == '8-Italian GP':
        st.markdown("""# Formula 1 - Italian GP 2020""")
        # SelectBox
        testdayno = st.selectbox("Select  Session",["Practice","Main Race"])

        if testdayno == "Practice":
            readme_text = st.markdown(read_markdown("8-Practice.md"))
            sessionno = st.radio("Select Practice Session",("Practice 1","Practice 2","Practice 3"))
            if sessionno =="Practice 1":
                if df_r8P1.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r8P1,True)
            elif sessionno =="Practice 2":
                if df_r8P2.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r8P2,True)
            elif sessionno =="Practice 3":
                if df_r8P3.empty:
                    st.write("Session Data is not available.")
                else:
                    load_plots(df_r8P3,True)
        elif testdayno == "Main Race":
            if df_r8M.empty:
                st.write("Session Data is not available.")
            else:
                #st.write(df_r8M.describe())
                load_plot2(df_r8M,1,59,75,150)
                load_plot3(df_r8M,75,90)
        else:
            st.write("Session Data is not available.")


    else:
        st.text('Select a page in the sidebar')
        

def load_plots(df,ispractice):
    #st.write(df.describe())
    if ispractice:
        sector = st.selectbox("Select Sector",["Overall","Sector 1","Sector 2","Sector 3"])
        #sectorno = "S123"
        if sector == "Overall":
            sectorno = "S123"
        elif sector == "Sector 1":
            sectorno = "S1"
        elif sector == "Sector 2":
            sectorno = "S2"
        elif sector == "Sector 3":
            sectorno = "S3"
        else:
            sectorno = "S123"

        maxlapval = df["LAPS"].max()
        rounded_maxlapsval = int(math.ceil(maxlapval / 5.0)) * 5

        meansectorval = df[sectorno].mean()
        rounded_meansectorval = (int(math.ceil(meansectorval / 5.0)) * 5)

        minsectorval = df[sectorno].min()
        rounded_minsectorval = int(math.floor(minsectorval / 5.0)) * 5

        maxectorval = df[sectorno].max()
        rounded_max123val = int(math.floor(maxectorval / 5.0)) * 5
        load_plot1(df,0,rounded_maxlapsval,rounded_minsectorval,rounded_max123val,sectorno)

        df = df[df[sectorno] < rounded_meansectorval]
        load_plot4(df,rounded_minsectorval,rounded_meansectorval,sectorno)

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

    elif session == 'r5P1':
        sessionfile = '5-Final_Practice1Data.json'
    elif session == 'r5P2':
        sessionfile = '5-Final_Practice2Data.json'
    elif session == 'r5P3':
        sessionfile = '5-Final_Practice3Data.json'
    elif session == 'r5M':
        sessionfile = '5-Final_MainRaceData.json'

    elif session == 'r6P1':
        sessionfile = '6-Final_Practice1Data.json'
    elif session == 'r6P2':
        sessionfile = '6-Final_Practice2Data.json'
    elif session == 'r6P3':
        sessionfile = '6-Final_Practice3Data.json'
    elif session == 'r6M':
        sessionfile = '6-Final_MainRaceData.json'

    elif session == 'r7P1':
        sessionfile = '7-Final_Practice1Data.json'
    elif session == 'r7P2':
        sessionfile = '7-Final_Practice2Data.json'
    elif session == 'r7P3':
        sessionfile = '7-Final_Practice3Data.json'
    elif session == 'r7M':
        sessionfile = '7-Final_MainRaceData.json'

    elif session == 'r8P1':
        sessionfile = '8-Final_Practice1Data.json'
    elif session == 'r8P2':
        sessionfile = '8-Final_Practice2Data.json'
    elif session == 'r8P3':
        sessionfile = '8-Final_Practice3Data.json'
    elif session == 'r8M':
        sessionfile = '8-Final_MainRaceData.json'

    if sessionfile != '':     
        with open(sessionfile) as json_file:
            jsondata = json.load(json_file)
        data = pd.DataFrame(jsondata)
    else:
        data = pd.DataFrame()
    return data

def load_plot1(df,startlap,endlap,mintime,maxtime,sectorno):
    df = df.sort_values(['N'],ascending=[1])
    fig = px.scatter(df, x="LAPS", y=sectorno, color="NAME",template="ggplot2",width=1200,height=600, hover_name="TYRE",trendline="lowess")
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
    st.text('Heatmap that indicate the total sector time for the main race. This gives an overview of push laps during the stint.')
    dataset = df.pivot("LAPNO", "DRIVERCODE", "S123")
    f, ax = plt.subplots(figsize=(25, 25))
    sns.heatmap(dataset, annot=True, cmap="cubehelix",vmin=mintime, vmax=maxtime, linewidths=0.5, fmt='g')
    sns.despine(left=True, bottom=True)
    st.pyplot()

def load_plot4(df,mintime,maxtime,sectorno):
    df = df.sort_values(['N'],ascending=[1])
    optiontyres = st.radio("By Tyre or Overall?",("Overall","By Tyre Category"))
    if optiontyres == "Overall":
        fig = px.box(df, x="NAME", y=sectorno,color ="NAME",width=1200,height=600)
        fig.update_xaxes(title_text='Name')
    if optiontyres =="By Tyre Category":
        fig = px.box(df, x="TYRECOMPOUND", y=sectorno,color="NAME",width=1200,height=600)
        fig.update_xaxes(title_text='Tyre Compounds')

    fig.update_yaxes(range=[mintime,maxtime],title_text='Total sector time')
   
    st.plotly_chart(fig)


def read_markdown(markdownfile):
    markdowncontentstr =""
    if markdownfile != "":
        markdowncontentstr = """{}""".format(open(markdownfile).read())
    return markdowncontentstr

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