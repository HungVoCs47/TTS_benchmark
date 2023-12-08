import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.title("Google Sheets as a DataBase")

#Function to create a sample Orders dataframe
def create_orders_dataframe():
    return pd.DataFrame({
        'Audio_1': ['a'],
        'Audio_2': ['a'],
        'Audio_3': ['a'],
        'Audio_4': ['a'],
        'Audio_5': ['a'],
        'Audio_6': ['a'],
        'Audio_7': ['a'],
        'Audio_8': ['a'],
        'Audio_9': ['a'], 
        'Audio_10': ['a'], 
        'Audio_11': ['a'],
        'Audio_12': ['a'],
        'Audio_13': ['a'],
        'Audio_14': ['a'],
        'Audio_15': ['a'],
        'Audio_16': ['a'],
        'Audio_17': ['a'],
        'Audio_18': ['a'],
        'Audio_19': ['a'],
        'Audio_20': ['a']
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
    
    df = conn.read(worksheet="IntelligibilityEvaluation")
    additional_data = {
        'Audio_1': ['c'],
        'Audio_2': ['b'],
        'Audio_3': ['a'],
        'Audio_4': ['a'],
        'Audio_5': ['a'],
        'Audio_6': ['a'],
        'Audio_7': ['a'],
        'Audio_8': ['a'],
        'Audio_9': ['a'], 
        'Audio_10': ['a'], 
        'Audio_11': ['a'],
        'Audio_12': ['a'],
        'Audio_13': ['a'],
        'Audio_14': ['a'],
        'Audio_15': ['a'],
        'Audio_16': ['a'],
        'Audio_17': ['a'],
        'Audio_18': ['a'],
        'Audio_19': ['a'],
        'Audio_20': ['a']
    }
    additional_df = pd.DataFrame(additional_data)
    updated_orders = df.append(additional_df, ignore_index=True)
    conn.update(worksheet="IntelligibilityEvaluation", data=updated_orders)
    st.success("Worksheet Updated 🤓")

if st.button("Clear Worksheet"):
    conn.clear(worksheet="IntelligibilityEvaluation")
    st.success("Worksheet Cleared 🧹")