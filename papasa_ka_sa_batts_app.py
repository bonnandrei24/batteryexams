import streamlit as st

st.set_page_config(layout="wide", page_title="Papasa Ka Sa Batts")

st.markdown(
    '''
    <style>
        .big-text {
            font-size: 5vw;
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

for _ in range(100):
    st.markdown('<div class="big-text">Papasa ka sa Batts</div>', unsafe_allow_html=True)
