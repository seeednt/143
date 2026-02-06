import streamlit as st

st.set_page_config(
    page_title="Anushri, will you be my valentine?",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🔥 NUKE STREAMLIT STYLING
st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        background-color: #f6c1cb !important;
    }

    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }

    iframe {
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=1000, scrolling=False)
