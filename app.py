import streamlit as st

st.set_page_config(
    page_title="Be My Valentine",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Remove Streamlit padding
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load your HTML
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=900, scrolling=False)
