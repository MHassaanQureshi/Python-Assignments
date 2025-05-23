import streamlit as st
import re


st.set_page_config(page_title="Password Strength Checker", layout="wide")


st.title("🔒 Password Strength Checker")


password = st.text_input("Enter your password here", type="password")


if password:
    score = 0
    messages = []

    
    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password should be at least **8 characters** long.")

    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Include both **uppercase and lowercase** letters.")

   
    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Add at least **one number (0-9)**.")

    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        messages.append("❌ Include at least **one special character** (!@#$%^&*).")

    
    if score == 4:
        st.success("✅ **Strong Password!**")
    elif score == 3:
        st.warning("⚠️ **Moderate Password - Consider adding more security features.**")
    else:
        st.error("❌ **Weak Password - Improve it using the suggestions below.**")

   
    if messages:
        for msg in messages:
            st.write(msg)
