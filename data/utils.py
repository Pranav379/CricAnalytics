import pandas as pd
import streamlit as st



@st.cache_data
def load_hawkeye_data():
    '''Reads in the hawkeye data csv and returns a pd Dataframe'''
    
    df = pd.read_csv("https://raw.githubusercontent.com/Aran203/cricanalytics/main/data/ipl-hawkeye-data.csv")
    return df