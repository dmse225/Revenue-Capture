import streamlit as st import pandas as pd import numpy as np import matplotlib.pyplot as plt 

Title

st.title("Healthcare Revenue Impact")

Sidebar filters

st.sidebar.header("Filters") category = st.sidebar.selectbox("Select Category", ["All", "Inpatient", "Outpatient", "Emergency"])

Sample DataFrame

data = { "Department": ["Cardiology", "Neurology", "Oncology", "Orthopedics"], "Revenue": [200000, 150000, 250000, 180000], "Category": ["Inpatient", "Outpatient", "Inpatient", "Emergency"] } df = pd.DataFrame(data)

Filter data

if category != "All": df = df[df["Category"] == category]

Display DataFrame

st.write("### Revenue Data", df)

Plot revenue

fig, ax = plt.subplots() ax.bar(df["Department"], df["Revenue"], color="skyblue") ax.set_xlabel("Department") ax.set_ylabel("Revenue ($)") ax.set_title("Revenue by Department") st.pyplot(fig)

st.write("---") st.write("Developed for healthcare financial analysis.")
