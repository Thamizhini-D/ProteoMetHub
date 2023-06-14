#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np
import streamlit as st

# calculates the concentration using the absorbance_value, m & c values  
def calconc (gradient, intercept, absorbance):
    concentration = (absorbance - intercept) / gradient
    return round(concentration, 3)

# calculates required volume to get the the desired amount of proteins from a sample under a particular condition
def calcvol (Protein_μg_aliquot, Aliquot_volume_μl, desired_protein_μg):
    required_volume = (desired_protein_μg*Aliquot_volume_μl)/Protein_μg_aliquot    
    return round(required_volume, 3)

# calculates the amount of proteins in the entire sample using aliquot amounts
def calcsampleconc (Protein_μg_aliquot, ALiquot_volume_μl, Sample_volume_ml):
    Sample_volume_μl = Sample_volume_ml*1000
    Protein_μg_sample = (Sample_volume_μl*Protein_μg_aliquot)/ALiquot_volume_μl
    return Protein_μg_sample


def data_processing(data):
    
    #standardizing verbal input by "SMALLER CASING" all of them
    data['Condition_name'] = data['Condition_name'].str.lower()
    data['Standard_Unknown'] = data['Standard_Unknown'].str.lower()
    
    #reading data from the columns
    conc = data[data.Standard_Unknown =='s']['Protein_μg_sample']
    abso = data[data.Standard_Unknown =='s']['Absorbance_nm']
    
    #line of best fit using polyfit function
    m, c = np.polyfit(conc, abso, 1)
    
    #group by Condition num/name, avg the abso values, name the new columns, round the avg values
    data_mean = data.groupby(['Condition_number'])['Absorbance_nm'].mean().round(3).rename('Average_absorbance_nm').reset_index()

    #merge the new column with the main index
    data = data.merge(data_mean)
    
    #calculate the amount of proteins using the absorbance values
    data.loc[data.Standard_Unknown =='u','Protein_μg_aliquot'] = calconc(m, c, data['Average_absorbance_nm'])
            
    #drop unnecessary columns
    data = data.drop(["Absorbance_nm", "Replicate_number"], 1)
    
   
    return st.write(data)

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




