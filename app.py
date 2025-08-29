import streamlit as st
import pandas as pd
from helpers import modify


st.set_page_config(page_title="FUT Tracker", page_icon="⚽")

st.markdown(
    """
    <style>
    /* Submit button */
    div.stButton > button:first-child {
        background-color: yellow;
        color: black;
        font-weight: bold;
        border: none;
        border-radius: 8px;
    }
    div.stButton > button:first-child:hover {
        background-color: #FFD700; /* darker yellow */
        color: black;
    }

    /* File uploader "Browse files" button */
    .stFileUploader button {
        background-color: yellow !important;
        color: black !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5em 1em !important;
    }
    .stFileUploader button:hover {
        background-color: #FFD700 !important; /* darker yellow */
        color: black !important;
    }
    
    /* Number input increment/decrement buttons */
    .stNumberInput button {
        background-color: yellow !important;
        color: black !important;
        border: none !important;
        border-radius: 4px !important;
        font-weight: bold !important;
    }
    .stNumberInput button:hover {
        background-color: #FFD700 !important; /* darker yellow */
        color: black !important;
    }
    
    
    </style>
    """,
    unsafe_allow_html=True
)


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



st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: yellow;
        color: black;
        text-align: center;
        padding: 10px;
        font-weight: bold;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
    }
    </style>
    <div class="footer">
        Made by <a href="https://github.com/a-jean-andreasian" target="_blank">@a_jean_andreasian</a>
    </div>
    """,
    unsafe_allow_html=True
)