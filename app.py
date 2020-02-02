import streamlit as st
import pandas as pd
import numpy as np
import json
import importlib
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px




def main():
    df = load_data()

    page = st.sidebar.selectbox("Choose a page", ['Homepage', 'Visualization', 'Prediction'])
    
    st.text('Select a page in the sidebar')

    if page == 'Homepage':
        st.title('Singapore Grandprix')
        st.text('Data set for the main race')
        st.dataframe(df)
    elif page == 'Visualization':
        st.title('Race data analysis')
        if st.checkbox('Show column descriptions'):
            st.dataframe(df.describe())
        sns.set(style="darkgrid")
        dataset = df.pivot("LAPNO", "DRIVERCODE", "S123")

        # Load Plots
        st.text('Heatmap using seaborn library')
        load_heatmp(dataset)
        st.text('Interactive Scatter using plotly library')
        load_plot1(df)

    else:
        st.title('In Progress...')
        

@st.cache
def load_data():
    jsondata = '{}'
    with open(r'singapore_data.json') as json_file:
        jsondata = json.load(json_file)
    data = pd.DataFrame(jsondata)
    return data


def load_heatmp(dataset):
    # Draw a heatmap with the numeric values in each cell
    f, ax = plt.subplots(figsize=(25, 25))
    sns.heatmap(dataset, annot=True, cmap="cubehelix",vmin=103, vmax=113, linewidths=0.5, fmt='g')
    sns.despine(left=True, bottom=True)
    st.pyplot()


def load_plot1(df):
    fig = px.scatter(df, x="LAPNO", y="S123", color="DRIVERCODE",width=1200,height=600)
    fig.update_xaxes(range=[0,65],title_text='Lap Number')
    fig.update_yaxes(range=[75,190],title_text='Total sector time')
    
    st.plotly_chart(fig)






if __name__ == '__main__':
    main()