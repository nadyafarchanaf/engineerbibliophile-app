import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from styles import load_css
from components.detail_book_page.header import render_header
from utils.db import load_data  # Import fungsi load data
from components.collection_book_page.collection_details import render_collection_page

st.set_page_config(page_title="Engineer Bibliophile", page_icon="📚", layout="wide")
load_css()
render_header()

df_buku = load_data()

if not df_buku.empty:
    render_collection_page(df_buku)