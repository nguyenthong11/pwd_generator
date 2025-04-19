import streamlit as st
import time
from generator import generate_password


st.set_page_config(page_title="Testing Password Generator", page_icon="🔐")
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