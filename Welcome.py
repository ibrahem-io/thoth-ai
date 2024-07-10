import streamlit as st
from utils.studio_style import apply_studio_style


if __name__ == '__main__':
    st.set_page_config(
        page_title="Nour AI"
    )
    apply_studio_style()
    st.title("إدارة محتوى السوشيال ميديا")
    st.markdown("نور هيساعدك تفكر وتعمل محتوى خاص بصفحتك على سوشيال ميديا" )