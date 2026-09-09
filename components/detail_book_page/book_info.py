import streamlit as st
import styles as styles

def render_left_column(buku):
    # 1. DEFINISIKAN VARIABEL DARI DICTIONARY 'BUKU' DI SINI
    judul = buku.get("Judul", "Tanpa Judul")
    penulis = buku.get("Penulis", "Anonim")
    tahun = buku.get("Tahun", "-")
    halaman = buku.get("Total_Halaman", "0")
    genre = buku.get("Genre", "-")
    kondisi = buku.get("Kondisi", "Baik")
    status_baca = buku.get("Status_Baca", "Belum Dibaca")
    progress_hlm = buku.get("Progress_Halaman", "0")
    lokasi = buku.get("Lokasi_Rak", "-")
    isbn = buku.get("ISBN", "-")
    tgl_beli = buku.get("Tanggal_Beli", "-")
    rating = buku.get("Rating", "5.0")
    store = buku.get("Lokasi_Beli_Buku", "Jakarta")

    
    # Data Peminjaman
    peminjam = buku.get("Peminjam", "")
    status_pinjam = buku.get("Status_Pinjam", "")

    # 2. VISUAL COVER BUKU
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #8A9A86 0%, #6E7E6A 100%); border-radius: 12px; padding: 20px; min-height: 250px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0px 4px 12px rgba(0,0,0,0.08);">
            <div>
                <span style="font-size: 11px; letter-spacing: 1px; color: #E2E8F0; font-weight: 600;">KOLEKSI PRIBADI</span>
                <span style="float: right; font-size: 12px; color: #FEFCBF;">★ {rating}</span>
                <h2 style="margin-top: 10px; color: #FFFFFF; font-size: 24px; font-weight: 700;">{judul}</h2>
                <p style="color: #F0FFF4; font-size: 14px; margin: 0;">{penulis} · {tahun}</p>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; color: #E2E8F0;">
                <span>{halaman} Halaman</span>
                <span>{genre}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
   
    # 4. DATA FISIK & AKUISISI
    # 1. Definisikan item-item data fisiknya dalam list
    items = [
        (styles.get_icon("location"), "Lokasi Penyimpanan", lokasi),
        (styles.get_icon("barcode"), "Nomor ISBN / EAN", isbn),
        (styles.get_icon("calendar"), "Tanggal Dibeli", tgl_beli),
        (styles.get_icon("store"), "Toko / Tempat Beli", store), # Ganti label jika perlu
    ]

    # 2. Render dengan perulangan bersih
    with st.container(border=True):
        st.markdown("<h4 style='color: #2D3748; margin-bottom: 15px;'>Data Fisik & Akuisisi</h4>", unsafe_allow_html=True)
        
        for idx, (icon, label, value) in enumerate(items):
            st.markdown(
                f"<div style='display:flex; align-items:center;'>{icon} <b style='color:#2D3748;'>{label}</b></div>"
                f"<div style='padding-left:28px; color:#718096; font-size:14px;'>{value}</div>", 
                unsafe_allow_html=True
            )
            
           # Garis tipis dengan margin rapat
        if idx < len(items) - 1:
            st.markdown("<hr style='margin: 10px 0; border: none; border-top: 5px solid #E2E8F0;'/>", unsafe_allow_html=True)