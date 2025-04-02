
import streamlit as st
import re

#page styling

st.set_page_config(page_title ="Password Streanght Checker", page_icon ="🔐", layout="centered")

#custom css

st.markdown("""
<style>
        .main {text-align: center;}
        .stTextInput {width: 60% !important; margin: auto;}
        .stButton button {width: 50%; background-color: #b7dfb9 color: white; font-size: 18px}
        .stButton buton:hover {background-color: #e00666;}
</style>
""", unsafe_allow_html=True)

#page title and discription

st.title("🔐 Password Streanght Checker")
st.write("Enter your Password below to check it security level. 🔎")

#function to check password stranght

def check_password_strength(password):
    score = 0
    feedback =[]
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should be include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should be add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should be include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        feedback.append("✅ Strong Password!")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")


    #feedback
    if feedback:
        with st.expander("Improve your Password"):
            for item in feedback:
                st.write(item)

# Get user input
password = st.text_input("Enter your password:", type="password", help="Ensure your Password is Strong")

#button working
if st.button("Check Strenght"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please entre your Password first")


        # Footer
st.markdown("---")
st.markdown("Created with 💕 By Afia Bakr using Streamlit")
