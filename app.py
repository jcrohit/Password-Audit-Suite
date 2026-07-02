import streamlit as st
from strength_checker import check_password_strength
from dictionary_generator import generate_dictionary
from hash_analyzer import generate_hashes
from bruteforce_simulator import estimate_bruteforce

st.set_page_config(page_title="Password Audit Suite", page_icon="🔐")

st.title("🔐 Password Audit Suite")

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Password Strength Analysis",
        "Dictionary Generator",
        "Hash Generator",
        "Brute Force Estimator"
    ]
)

if menu == "Password Strength Analysis":
    password = st.text_input("Enter Password", type="password")
    if st.button("Analyze"):
        result = check_password_strength(password)
        st.write(result)

elif menu == "Dictionary Generator":
    name = st.text_input("Name")
    year = st.text_input("Year")
    if st.button("Generate"):
        result = generate_dictionary(name, year)
        st.write(result)

elif menu == "Hash Generator":
    password = st.text_input("Password", type="password")
    if st.button("Generate Hashes"):
        result = generate_hashes(password)
        st.json(result)

elif menu == "Brute Force Estimator":
    length = st.number_input("Password Length", min_value=1, value=8)
    if st.button("Estimate"):
        result = estimate_bruteforce(length)
        st.write(result)