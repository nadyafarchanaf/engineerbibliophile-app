import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from styles import load_css
from components.detail_book_page.header import render_header
from components.detail_book_page.book_info import render_left_column
from components.detail_book_page.book_details import render_right_column
from utils.db import load_data  # Import fungsi load data

# 1. Konfigurasi
st.set_page_config(page_title="Engineer Bibliophile", page_icon="📚", layout="wide")
load_css()
render_header()

# 2. Tarik Data dari Spreadsheet
df_buku = load_data()

# 3. Cek apakah data berhasil ditarik
# ✅ KODE BENAR:
if not df_buku.empty:
    buku_terpilih = df_buku.iloc[0].to_dict() # Ambil baris pertama saja
    
    left_col, right_col = st.columns([1.2, 2.2])
    with left_col:
        render_left_column(buku_terpilih)
    with right_col:
        render_right_column(buku_terpilih)
else:
    st.warning("Data buku kosong atau spreadsheet belum terhubung dengan benar.")