import streamlit as st
from tax_engine import estimate_total_tax

st.title("US Tax Estimator")

st.write("Estimate federal, state, and local taxes based on income and location.")

# user inputs
income = st.number_input("Income ($)", min_value=0, value=100000)

state = st.text_input("State (example: VA)")

county = st.text_input("County (example: Arlington)")

# button to calculate
if st.button("Estimate Taxes"):

    result = estimate_total_tax(income, state, county)

    st.subheader("Tax Breakdown")

    st.write("Federal Tax:", result["federal"])
    st.write("State Tax:", result["state"])
    st.write("Local Tax:", result["local"])
    st.write("Payroll Tax:", result["payroll"])
    st.write("Sales Tax:", result["sales"])
    st.write("Property Tax:", result["property"])

    st.write("Total Taxes:", result["total"])
    st.write("Effective Tax Rate:", result["effective_rate"])

    st.write("After Tax Income:", result["leftover"])
