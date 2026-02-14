import streamlit as st
import pandas as pd
import seaborn as sns
st.title("Data Analysis")
st.subheader("Data Analysis Using Python and Streamlit")
upload=st.file_uploader("Upload your dataset in csv")
if upload is not None:
    data=pd.read_csv(upload)
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)

if upload is not None:
    data_shape=st.radio("What Dimension to check?",("Rows","Columns"))
    if data_shape=="Rows":
        st.text("Number of Rows:")
        st.write(data.shape[0])
    if data_shape=="Columns":
        st.text("Number of Columns")
        st.write(data.shape[1])

if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the Dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations! No null values")

if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset contains some duplicate values")
        dup=st.selectbox("Do you want to remove duplicates?", ("Select One","Yes","No")
                         )
        if dup=="Yes":
            data=data.drop.duplicates()
            st.text("Duplicates Removed")
        if dup=="No":
            st.text("No problem")
    else:
        st.success("No duplicates!!")

if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include="all"))

if st.button("About App"):
    st.text("This app was a beginner data science project with the help of Streamlit")

if st.button("By"):
    st.success("Done by Roselyn Sunil")
