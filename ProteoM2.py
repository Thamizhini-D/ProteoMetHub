#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np
import streamlit as st
from streamlit_jupyter import StreamlitPatcher, tqdm

StreamlitPatcher().jupyter()  # register streamlit with jupyter-compatible wrappers
st.title("ProteoMetrics")
st.subheader("Created for the Bradford Assay")

uploaded_file = st.file_uploader("Upload your file", type=("csv", "xls", "xlsx"))

if uploaded_file is not None:
    for filename in uploaded_file.name:
        extension = file_name.split('.')[1]
        
        if (extension == 'csv'):
                dataframe = pd.read_csv(uploaded_file)

            
        elif (extension == 'xlsx' or extension == 'xls'):
                dataframe = pd.read_excel(uploaded_file)


        st.write(dataframe)


# In[ ]:




