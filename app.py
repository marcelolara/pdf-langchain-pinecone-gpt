from dotenv import load_dotenv
import streamlit as st


def main():
    load_dotenv()
    st.set_page_config(page_title='Pregunta a tu PDF')
    st.header('Pregunta a tu PDF 💬')

    # upload file
    pdf = st.file_uploader('Sube tu PDF', type='pdf')

if __name__ == '__main__':
  main()