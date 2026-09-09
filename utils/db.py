import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

@st.cache_data(ttl=60)  # Simpan cache selama 60 detik agar web tidak sering me-reload sheet
def load_data():
    """Mengambil seluruh baris data dari Google Sheet dan mengembalikannya sebagai Pandas DataFrame"""
    try:
        # Koneksi ke Google Sheets memakai URL dari secrets.toml
        conn = st.connection("gsheets", type=GSheetsConnection)
        
        # Membaca sheet pertama (ttl=0 jika ingin selalu ter-update otomatis)
        df = conn.read(ttl=0)
        
        # Membersihkan kolom dari nilai kosong jika ada
        df = df.dropna(how="all")
        return df
    except Exception as e:
        st.error(f"Gagal mengambil data dari Google Sheets: {e}")
        return pd.DataFrame()