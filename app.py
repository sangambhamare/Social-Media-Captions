import streamlit as st

# Title and header
st.title("Customer Information Form")
st.header("Please enter your details:")

# Input fields
name = st.text_input("Full Name:")
email = st.text_input("Email Address:")
phone_number = st.text_input("Phone Number:")
country = st.selectbox("Country:", ["USA", "Canada", "UK", "Other"])
if country == "Other":
    other_country = st.text_input("Please specify:")
else:
    other_country = ""

# Checkbox for additional information
more_info = st.checkbox("Do you want to share additional information?")
if more_info:
    address = st.text_area("Address:")
    occupation = st.text_input("Occupation:")
    interests = st.multiselect("Interests:", ["Travel", "Reading", "Cooking", "Sports"])

# Submit button and message
submit_button = st.button("Submit")

if submit_button:
    # Display the collected information
    st.success("Thank you for submitting your information!")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Phone number: {phone_number}")
    st.write(f"Country: {country}")
    if other_country:
        st.write(f"- Other country: {other_country}")
    if more_info:
        st.write(f"Address: {address}")
        st.write(f"Occupation: {occupation}")
        st.write(f"Interests: {', '.join(interests)}")


