import streamlit as st

def render_header():
    col1, col2, col3 = st.columns([6, 2, 2])
    with col1:
        st.title("Detail & Catatan Koleksi")
    with col2:
        st.button("Kembali ke Koleksi", use_container_width=True)
    with col3:
        st.button("Ubah Status / Lokasi", type="secondary", use_container_width=True)
    st.write("")