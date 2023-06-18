#### ProteoMetHub
# **ProteoMetrics🧪**
###### _Made for the Bradford Assay_ ✨

This app has been created to be used in conjunction with the Bradford Assay. 
The user is to upload the experimental data in a specific Excel file format. This is to to ensure that inputted data has been standardized to be used for processing with this tool. 

#### Workflow:
1. The user is to submit an excel file containing known concentrations and their respective absorbance values **in the required format!**
2. It must also contain absorbances for samples with unknown concentration. **Refer to the Excel file format rules to learn how to fill cells with unknown values!**           Excel template also consists rules for how to differentiate between data taken from Standard solutions and Unknown samples.
3. The tool constructs a standard curve graph with the data from Standard solutions. It also conducts a linear regression analysis calculating gradient and C-intercept values. **Take special care in labelling which entries are standard solutions since the calculated gradient and c-intercept values will depend on this.**
4. Using the inputted data, gradient and C-intercept values, it can construct a linear equation. This equation can be used to calculate the unknown concentrations. Additionally, the tool is also able to output the average absorbance value and provide the amount of volume required to get a specific amount of protein. **The amount is defaulted to 100micrograms**.
5. The app allows the user to download their processed data results in a csv file and the standard curve graph in a png file.

