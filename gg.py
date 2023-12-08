import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.title("Google Sheets as a DataBase")

#Function to create a sample Orders dataframe
def create_orders_dataframe():
    return pd.DataFrame({
        'OrderID': [101, 102, 103, 104, 105],
        'CustomerName': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'ProductList': ['ProductA, ProductB', 'ProductC', 'ProductA, ProductC', 'ProductB, ProductD', 'ProductD'],
        'TotalPrice': [200, 150, 250, 300, 100],
        'OrderDate': ['2023-08-18', '2023-08-19', '2023-08-19', '2023-08-20', '2023-08-20']
    })

# Create the Orders dataframe
orders = create_orders_dataframe()

# Update the TotalPrice column in the orders dataframe to create updated_orders
updated_orders = orders.copy()
updated_orders['TotalPrice'] = updated_orders['TotalPrice'] * 100

with st.expander("Data ⤵"):
    st.write("Orders")
    st.dataframe(orders)
    st.write("Updated Orders")
    st.dataframe(updated_orders)

st.divider()
st.write("CRUD Operations:")
# Establishing a Google Sheets connection
conn = st.connection("gsheets", type=GSheetsConnection)

if st.button("New Worksheet"):
    conn.create(worksheet="Orders", data=orders)
    st.success("Worksheet Created 🎉")

if st.button("Update Worksheet"):
    
    updated_orders = orders.copy()
    additional_data = {'OrderID': [107],
        'CustomerName': ['Hung Vo'],
        'ProductList': ['D'],
        'TotalPrice': [100],
        'OrderDate': ['2023-08-18']}
    additional_df = pd.DataFrame(additional_data)
    updated_orders = updated_orders.append(additional_df, ignore_index=True)
    conn.update(worksheet="Orders", data=updated_orders)
    st.success("Worksheet Updated 🤓")

if st.button("Clear Worksheet"):
    conn.clear(worksheet="Orders")
    st.success("Worksheet Cleared 🧹")