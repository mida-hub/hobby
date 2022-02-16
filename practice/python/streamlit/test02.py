import streamlit as st
import pandas as pd
import requests
import os
from slack_sdk import WebClient
from html2image import Html2Image

hti = Html2Image(custom_flags=['--virtual-time-budget=3000'])
client = WebClient(os.environ["SLACK_BOT_TOKEN"])

def common():
    st.title('Title')
    st.write("Document")
    st.table(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))

    st.markdown('# Markdown 1st')
    st.markdown('## Markdown    2nd')
    st.latex(r'\bar{X} = \frac{1}{N} \sum_{n=1}^{N} x_i')

def page1():
    st.write("Here is page 1.")

    if st.button('To Slack'):
        st.write('Why hello there')

        # upload_text_file = client.files_upload(
        #     channels='#github-actions',
        #     title="sample.png",
        #     file="./sample.png",
        #     initial_comment="Here is the file:",
        # )

        hti.screenshot(url='http://localhost:8501',
                       save_as='ss_sample.png',
                       )

def page2():
    st.write("Here is page 2.")
    common()

def main():
    with st.sidebar:
        page = st.radio('Link', ('page1', 'page2'), )

    if page == 'page1':
        page1()
    elif page == 'page2':
        page2()

main()
