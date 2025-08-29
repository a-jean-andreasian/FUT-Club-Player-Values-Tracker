import streamlit as st
import pandas as pd
from helpers import modify

st.title("FUT Club Player Values Tracker")

file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"],
    help="To generate the report you can use a browser extension, e.g. FutNext"
)

num_of_rows = st.number_input(
    "Number of rows to display", min_value=1, value=10, step=1
)

min_price = st.number_input(
    "Minimum price", min_value=1, value=250000, step=1
)

tradables_only = st.checkbox('Show tradable players only', value=False)

if st.button("Submit", type="primary", use_container_width=True):
    if not file:
        st.warning("Please upload a CSV file before submitting.")
    else:
        try:
            df = pd.read_csv(file)
        except Exception as e:
            st.error(f"Error reading the CSV file: {e}")
        else:
            try:
                result = modify(df=df, num_of_rows=num_of_rows, min_price=min_price, tradables_only=tradables_only)
            except Exception as e:
                st.error(f"Error processing the data: {e}")
            else:
                st.dataframe(result, use_container_width=True)
