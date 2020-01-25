import streamlit as st
import pandas as pd
import numpy as np
import json
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px




def main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    df = load_data()

    page = st.sidebar.selectbox("Choose a page", ['Homepage', 'Exploration', 'Prediction'])

    if page == 'Homepage':
        st.title('Singapore Grandprix')
        st.text('Select a page in the sidebar')
        st.dataframe(df)
    elif page == 'Exploration':
        if st.checkbox('Show column descriptions'):
            st.dataframe(df.describe())
        sns.set(style="darkgrid")
        dataset = df.pivot("LAPNO", "DRIVERCODE", "S123")

        # Draw a heatmap with the numeric values in each cell
        f, ax = plt.subplots(figsize=(19, 25))
        sns.heatmap(dataset, annot=True, cmap="cubehelix",vmin=103, vmax=113, linewidths=0.5, fmt='g')
        sns.despine(left=True, bottom=True)
        st.pyplot()
        
        
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

def load_plot1(df):
    
    
    fig = px.scatter(df, x="LAPNO", y="S123", color="DRIVERCODE")
    fig.update_yaxes(range=[77,189])
    st.plotly_chart(fig)






if __name__ == '__main__':
    main()