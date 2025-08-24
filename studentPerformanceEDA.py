import pandas as pd
import seaborn as sns
import matplotlib as plt
import streamlit as st
import os


# --- Step 1: Project Setup and Data Acquisition ---
# Note: This code assumes the 'students_performance.csv' file is
# located in a 'data' directory relative to this script.

# --- Step 2: Exploratory Data Analysis (EDA) ---

# create a function to load data
#  cache the data to avoid re-loading on every inetraction
@st.cache_data
def load_data(file_path):
    """
    Loads the student performance dataset from a given file path.
    :param file_path:
    :return:
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"error: the file '{file_path}'not found")
        st.stop()

# Define the file path
# Define the file path
file_path = "/Users/shaveta.bali/Documents/digicrome-internship-01-25-eda-project-04-25-EDA/data/student_habits_performance.csv"


# Load the data
df = load_data(file_path)

# check if the data was loaded successfully
if df is not None:
#---Initial Inspection -----
    st.sidebar.header("DataInspection")
    if st.sidebar.checkbox("Show Raw Data"):
        st.subheader("Raw Data(First 5 Rows)")
        st.write(df.head())
        st.subheader("Data Shape")
        st.write(df.shape)
        st.subheader("Data Info")
        st.write(df.info())
        st.subheader("Descriptive statistics")
        st.write(df.describe(include='all)'))
# --------------Data Cleaning and preprocessing ---------------
# Rename columns for clarity (replacing spaces with underscores)
df.columns = df.columns.str.replace(" ","_")

# Check for missing values and duplicates
st.sidebar.subheader("Data Quality Check")
if st.sidebar.checkbox("check for missing Values and Duplicates"):
    st.subheader("Missing values")
    st.write(df.isnull().sum())
    st.subheader("Duplicate Rows")
    st.write(f"Number of duplicate rows: {df.duplicated().sum()}")


# ---------Step 3 . Building the streamlit application -----
# set up the app layout
    st.title( "studenty Performance Analysis & visualization ")
    st.markdown("his interactive dashboard explores the **Student Performance in Exams** dataset from Kaggle. "
                "Use the filters in the sidebar to uncover insights!")



