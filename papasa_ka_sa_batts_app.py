import streamlit as st

st.set_page_config(layout="wide", page_title="Papasa Ka Sa Batts")

st.markdown(
    '''
    <style>
        .big-text {
            font-size: 2vw;
            color: #00ff00;
            text-align: center;
        }
        body {
            background-color: black;
        }
    </style>
    ''',
    unsafe_allow_html=True
)

for i in range(1, 1665):
    st.markdown(f'<div class="big-text">{i}. Papasa ka sa Batts</div>', unsafe_allow_html=True)
