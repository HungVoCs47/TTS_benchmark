import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.title("Google Sheets as a DataBase")

#Function to create a sample Orders dataframe
def create_orders_dataframe():
    return pd.DataFrame({
        'Audio_1': [],
        'Audio_2': [],
        'Audio_3': [],
        'Audio_4': [],
        'Audio_5': [],
        'Audio_6': [],
        'Audio_7': [],
        'Audio_8': [],
        'Audio_9': [], 
        'Audio_10': [], 
        'Audio_12': [],
        'Audio_13': [],
        'Audio_14': [],
        'Audio_15': [],
        'Audio_16': [],
        'Audio_17': [],
        'Audio_18': [],
        'Audio_19': [],
        'Audio_20': []
    })

# Create the Orders dataframe
orders = create_orders_dataframe()

# Update the TotalPrice column in the orders dataframe to create updated_orders



st.divider()
st.write("CRUD Operations:")
# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

if st.button("New Worksheet"):
    conn.create(worksheet="IntelligibilityEvaluation", data=orders)
    st.success("Worksheet Created 🎉")

if st.button("Update Worksheet"):
    
    df = conn.read(worksheet="Orders")
    additional_data = {'OrderID': [107],
        'CustomerName': ['Hung Vo'],
        'ProductList': ['D'],
        'TotalPrice': [100],
        'OrderDate': ['2023-08-18']}
    additional_df = pd.DataFrame(additional_data)
    updated_orders = df.append(additional_df, ignore_index=True)
    conn.update(worksheet="Orders", data=updated_orders)
    st.success("Worksheet Updated 🤓")

if st.button("Clear Worksheet"):
    conn.clear(worksheet="Orders")
    st.success("Worksheet Cleared 🧹")