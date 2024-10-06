import streamlit as st
import pandas as pd
from data_loader import load_data

def main():
    st.title("Loan Default Predictor")

    # Add sidebar for data loading
    st.sidebar.title("Data Loading")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.sidebar.success("Data loaded successfully!")
        except Exception as e:
            st.sidebar.error(f"Error: {e}")
            return
    else:
        try:
            df = load_data()
        except Exception as e:
            st.error(f"Failed to load default data: {e}")
            return

    # Display the first few rows of the data
    st.subheader("Dataset Overview")
    st.write(df.head())

if __name__ == "__main__":
    main()