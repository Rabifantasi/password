import streamlit as st
import re

def check_password_strength(password):
    score = 0
    remarks = ""

    # Criteria for password strength
    if len(password) >= 8:  # Length check
        score += 1
    if re.search(r"[A-Z]", password):  # Uppercase letter check
        score += 1
    if re.search(r"[a-z]", password):  # Lowercase letter check
        score += 1
    if re.search(r"\d", password):  # Digit check
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # Special character check
        score += 1

    # Strength rating
    if score == 0:
        remarks = "Very Weak 😞"
    elif score == 1:
        remarks = "Weak 🙁"
    elif score == 2:
        remarks = "Moderate 😐"
    elif score == 3:
        remarks = "Strong 🙂"
    elif score == 4:
        remarks = "Very Strong 💪"
    elif score == 5:
        remarks = "Excellent 🔥"

    return remarks

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    strength = check_password_strength(password)
    st.write(f"**Strength:** {strength}")
