import streamlit as st

st.set_page_config(
    page_title="Anushri 💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    html, body {
        height: 100%;
        overflow: hidden !important;
        background-color: #f6c1cb !important;
    }

    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        height: 100vh !important;
    }

    header, footer, #MainMenu {
        display: none !important;
    }

    iframe {
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        overflow: hidden !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=1000, scrolling=False)
