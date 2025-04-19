import streamlit as st
from generator import generate_password


st.set_page_config(page_title="Testing Password Generator", page_icon="🔐")
st.title("🔐 Password Generator")

seed = st.text_input("Enter seed string:")
length = st.number_input("Desired password length", min_value=4, value=15)


if st.button("Generate Password"):
    password = generate_password(length, seed)
    st.success(f"Generated password: `{password}`")

    st.code(password, language="text")
    # Copy button using custom JavaScript

    st.markdown(f"""
    <script>
    navigator.clipboard.writeText("{password}");
    if (btn) {{
        btn.innerText = "✅ Copied!";
    }}
    </script>
    """, unsafe_allow_html=True)