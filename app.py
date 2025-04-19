import streamlit as st
import time
from generator import generate_password

st.title("🔐 Password Generator")

seed = st.text_input("Enter seed string:")
length = st.number_input("Desired password length", min_value=4, value=15)

if st.button("Generate Password"):
    password = generate_password(length, seed)
    st.success(f"Generated password: `{password}`")

    st.code(password, language="text")
    # Copy button using HTML/JS
    st.markdown(f"""
    <button onclick="navigator.clipboard.writeText('{password}');
                    fetch('/?copied=true')"
            style="
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 14px;
                margin-top: 10px;
                border-radius: 5px;
                cursor: pointer;">
        📋 Copy to Clipboard
    </button>
    """, unsafe_allow_html=True)

    # Set the flag manually via hidden form
    st.form(key="copied_form")
    st.session_state["copied"] = True
    st.experimental_rerun()

# Show the "Copied!" message if the flag is set
if st.session_state["copied"]:
    st.success("✅ Copied!")
    time.sleep(2)
    st.session_state["copied"] = False
    st.experimental_rerun()