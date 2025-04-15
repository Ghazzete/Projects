import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.markdown("🔐 **Password Strength Checker**")
st.markdown("""
## Welcome to the ultimate password strength checker! 🤚

Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
We will give you helpful tips to create a **strong password** 🔐
""")

password = st.text_input("Enter your password", type="password")

feedback = []
score = 0

if password:
    # Check for length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")
    
    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")
    
    # Check for special characters
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%&*).")

    # Strength Feedback
    st.markdown("## Password Strength Result")
    if score == 4:
        st.success("✔ Your password is strong!")
    elif score == 3:
        st.warning("🟡 Your password is medium strength. It could be stronger.")
    else:
        st.error("🔴 Your password is weak. Please make it stronger.")

    # Suggestions
    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started.")
