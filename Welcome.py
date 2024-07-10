import streamlit as st
from utils.studio_style import apply_studio_style


if __name__ == '__main__':
    st.set_page_config(
        page_title="Thoth AI"
    )
    apply_studio_style()
    st.title("AI for Business Excellence")
    st.markdown("Beta Version v0.1" )