#!/usr/bin/env python
# coding: utf-8

# In[25]:
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import io 

st.set_page_config(page_title='ProteoMetrics', page_icon="🧪", layout="centered", initial_sidebar_state="auto", menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    })
        
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

        
def standard_curve_data(data):
     #standardizing verbal input by "SMALLER CASING" all of them
    data['Condition_name'] = data['Condition_name'].str.lower()
    data['Standard_Unknown'] = data['Standard_Unknown'].str.lower()

    #reading data from the columns
    conc = data[data.Standard_Unknown =='s']['Protein_μg_sample']
    abso = data[data.Standard_Unknown =='s']['Absorbance_nm']
    return conc, abso

def intergrad_calc(conc, abso):
   #line of best fit using polyfit function
    m, c = np.polyfit(conc, abso, 1)
    return m, c
    
def draw_graph(conc_x, abso_y, grad_m, inter_c):
           st.divider()
           st.header("Linear Regression Model")

           fig, ax = plt.subplots(figsize=(6,4))

           plt.ylabel('Absorbance at 595nm')
           plt.xlabel('Amount of proteins (μg)')
           plt.title('Graph of the standard curve')

           # plot the line of best fit
           plt.plot(conc_x, abso_y, 'o')
           # plot the line of best fit
           plt.plot(conc_x, grad_m*conc_x+inter_c, 'g-')
           return fig
    
def data_process_table(data, m, c):
            
    st.divider()

    st.header("Processed Data")
    st.markdown("Calculates average absorbance value per concentration, amount of proteins in aliquot and sampls and the volume needed for 100μg of proteins")

    #group by Condition num/name, avg the abso values, name the new columns, round the avg values
    data_mean = data.groupby(['Condition_number'])['Absorbance_nm'].mean().round(3).rename('Average_absorbance_nm').reset_index()

    #merge the new column with the main index
    data = data.merge(data_mean)
    
    #calculate the amount of proteins using the absorbance values
    data.loc[data.Standard_Unknown =='u','Protein_μg_aliquot'] = calconc(m, c, data['Average_absorbance_nm'])
            
    #drop unnecessary columns
    data = data.drop(columns=['Absorbance_nm', 'Replicate_number'], axis=1)
    
    #drop repetetive rows
    data.drop_duplicates(['Condition_number', 'Condition_name'], keep='first', inplace=True)
    data.reset_index(drop=True, inplace=True)
            
    #calculate volume to get desired amount of proteins. Default set to 100μg
    data.loc[data.Standard_Unknown =='u', ['Volume_(μl)_for_100μg']] = calcvol (data['Protein_μg_aliquot'], data['Aliquot_volume_μl'], 100)
            
    #calculate the amount of protein in entire sample based on amounts in aliquot 
    data.loc[data.Standard_Unknown =='u','Protein_μg_sample'] = calcsampleconc(data['Protein_μg_aliquot'], data['Aliquot_volume_μl'], data['Sample_volume_ml'])
    
    return data

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


st.title("ProteoMetrics")
st.caption("...for for the Bradford Assay")

uploaded_file = st.file_uploader("Upload your file", type=("csv", "xls", "xlsx"))

if uploaded_file is not None:
    file_name = uploaded_file.name
    extension = file_name.split('.')[1]
        
    if (extension == 'csv'):
            dataframe = pd.read_csv(uploaded_file)

            
    elif (extension == 'xlsx' or extension == 'xls'):
            dataframe = pd.read_excel(uploaded_file)

    st.header("Your Experimental Data")
    st.markdown("Check if your data is displayed correctly, i.e. has been entered according to the set format")

    st.write(dataframe)
    if st.button("Process data"):
        conc_abso = standard_curve_data(dataframe)
        m_c_output = intergrad_calc(conc_abso[0], conc_abso[1])
        process_result = data_process_table(dataframe, m_c_output[0], m_c_output[1])  
        st.write(process_result)
        
        graph_result = draw_graph(conc_abso[0], conc_abso[1], m_c_output[0], m_c_output[1])
        st.pyplot(graph_result)    
        img = io.BytesIO()
        graph_result.savefig(img, format='png')

        btn = st.download_button(
           label="Download image",
           data=img,
           mime="image/png"
        )
            
        
        st.download_button(
                label="Download CSV",
                data=convert_df(process_result),
                mime='text/csv',
                )  

        


        






        
        

            
   
        
# In[ ]:





