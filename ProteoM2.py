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
    filename = uploaded_file.name
    st.write(filename)



# In[ ]:




