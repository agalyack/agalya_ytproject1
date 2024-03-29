import streamlit as st
import pandas
from page1 import page as page1
from page2 import page as page2

PAGES = {
    "Page 1": page1,
    "Page 2": page2
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == '__main__':
    main()
