import streamlit as st
from utils.db import load_data
from components.storage_book_page.storage_book import render_storage_page

df_buku = load_data()

if not df_buku.empty:
    render_storage_page(df_buku)