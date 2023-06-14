#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np
import streamlit as st
from streamlit_jupyter import StreamlitPatcher, tqdm

def data_processing(data):
    
    #standardizing verbal input by "SMALLER CASING" all of them
    data['Condition_name'] = data['Condition_name'].str.lower()
    data['Standard_Unknown'] = data['Standard_Unknown'].str.lower()
    return st.write(data)

StreamlitPatcher().jupyter()  # register streamlit with jupyter-compatible wrappers
st.title("ProteoMetrics")
st.subheader("Created for the Bradford Assay")

uploaded_file = st.file_uploader("Upload your file", type=("csv", "xls", "xlsx"))

if uploaded_file is not None:
    file_name = uploaded_file.name
    extension = file_name.split('.')[1]
        
    if (extension == 'csv'):
            dataframe = pd.read_csv(uploaded_file)

            
    elif (extension == 'xlsx' or extension == 'xls'):
            dataframe = pd.read_excel(uploaded_file)


    st.write(dataframe)
    if st.button("Process data"):
        data_processing(dataframe)
# In[ ]:




