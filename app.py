import streamlit as st
from generator import PasswordGenerator

st.set_page_config(page_title="Password Generator from Seed", page_icon="🔐")
st.title("🔐 Password Generator")

"""
This app generates a robust password using the seed string.
"""

seed = st.text_input("Enter seed string:", type="password")  # Hide seed input
length = st.number_input("Desired password length", min_value=4, max_value=72, value=15)


if st.button("Generate Password"):

    pwd_gen = PasswordGenerator(length=length, seed_seq=seed)
    pwd_gen.generate_password()
    if not pwd_gen.check:
        st.warning("⚠️ change seed string or length for more secure password")
        
    # Store in session state
    st.session_state.password = pwd_gen.pw
    st.success("✅ Generated password: ")

    st.code(pwd_gen.pw, language="text")
