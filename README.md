#### ProteoMetHub
# **ProteoMetrics🧪**
###### _Made for the Bradford Assay_ ✨

This app has been created to be used in conjunction with the Bradford Assay. It is commonly used for protein quantification in the field of Biochemistry. Having said that, conducting this experiment and having to manually process the data from it may be a routine task in some labs. This tool is created to address those needs in specific. Looking for an error-free, automated solution? Say no more. ProteoMetrics here, to save the day!


#### Workflow:
1. The user is to upload the experimental data in a specific Excel file format. This is to to ensure that inputted data has been standardized to be used for processing with this tool. 
2. The user is to submit an excel file containing known concentrations and their respective absorbance values _in the required format!_
3. It must also contain absorbances for samples with unknown concentration. _Refer to the Excel file format rules to learn how to fill cells with unknown values!_          Excel template also consists rules for how to differentiate between data taken from Standard solutions and Unknown samples.
4. The tool constructs a standard curve graph with the data from Standard solutions. It also conducts a linear regression analysis calculating gradient and C-intercept values. _Take special care in labelling which entries are standard solutions since the calculated gradient and c-intercept values will depend on this._
5. Using the inputted data, gradient and C-intercept values, it can construct a linear equation. This equation can be used to calculate the unknown concentrations. Additionally, the tool is also able to output the average absorbance value and provide the amount of volume required to get a specific amount of protein. _The amount is defaulted to 100micrograms._
6. The app allows the user to download their processed data results in a csv file and the standard curve graph in a png file.

**Take special care in uploading the data in the required units. This is mentioned in the provided Excel template.**



