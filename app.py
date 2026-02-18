import streamlit as st
from generator import generate_password

st.set_page_config(page_title="Password Generator from Seed", page_icon="🔐")
st.title("🔐 Password Generator")

"""
This app generates a robust password using the seed string.
"""

seed = st.text_input("Enter seed string:", type="password")  # Hide seed input
length = st.number_input("Desired password length", min_value=4, max_value=72, value=15)


if st.button("Generate Password"):
    check_good, password = generate_password(length, seed)
    if not check_good:
        st.warning("⚠️ change seed string or length for more secure password")
        
    # Store in session state
    st.session_state.password = password
    st.success("✅ Generated password: ")

    st.code(password, language="text")

    # Separate copy button
# if 'password' in st.session_state:
#     if st.button("📋 Copy to Clipboard"):
#         try:
#             pyperclip.copy(st.session_state.password)
#             st.success("Copied!")
#         except:
#             st.error("Copy failed - please copy manually")
