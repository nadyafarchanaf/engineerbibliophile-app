import streamlit as st
from styles import get_icon

def render_collection_page(df_buku):
    # --- HEADER ---
    col_header, col_btn = st.columns([4, 1])
    with col_header:
        st.title("Koleksi Buku")

    # --- FILTER BOX ---
    with st.container(border=True):
        # 1. Quick Filter Pills (Pilihan Kategori Quick)
        total_buku = len(df_buku)
        tersedia = len(df_buku[df_buku['Status_Pinjam'].str.lower() != 'dipinjam']) if 'Status_Pinjam' in df_buku else 0
        dipinjam = len(df_buku[df_buku['Status_Pinjam'].str.lower() == 'dipinjam']) if 'Status_Pinjam' in df_buku else 0
        dibaca = len(df_buku[df_buku['Status_Baca'].str.lower() == 'sedang dibaca']) if 'Status_Baca' in df_buku else 0

        st.pills(
            label="Kategori",
            options=[
                f"Semua Koleksi ({total_buku})",
                f"Tersedia di Rak ({tersedia})",
                f"Sedang Dipinjam ({dipinjam})",
                f"Sedang Dibaca ({dibaca})"
            ],
            default=f"Semua Koleksi ({total_buku})",
            label_visibility="collapsed"
        )
        
        st.write("")

        # 2. Filter Baris Kedua (Search & Dropdowns)
        f1, f2, f3, f4 = st.columns([2, 1.5, 1.5, 1.5])
        
        with f1:
            search_query = st.text_input("Cari Judul / Penulis", placeholder="Misal: Pramoedya, Filosofi...")
        with f2:
            lokasi_opts = ["Semua"] + list(df_buku["Lokasi_Rak"].unique()) if "Lokasi_Rak" in df_buku else ["Semua"]
            opt_lokasi = st.selectbox("Lokasi Penyimpanan", lokasi_opts)
        with f3:
            progres_opts = ["Semua"] + list(df_buku["Status_Baca"].unique()) if "Status_Baca" in df_buku else ["Semua"]
            opt_progres = st.selectbox("Progres Baca", progres_opts)
        with f4:
            kondisi_opts = ["Semua"] + list(df_buku["Kondisi"].unique()) if "Kondisi" in df_buku else ["Semua"]
            opt_kondisi = st.selectbox("Kondisi Fisik", kondisi_opts)

    # --- FILTERING LOGIC ---
    df_filtered = df_buku.copy()
    
    if search_query:
        df_filtered = df_filtered[
            df_filtered['Judul'].astype(str).str.contains(search_query, case=False, na=False) |
            df_filtered['Penulis'].astype(str).str.contains(search_query, case=False, na=False)
        ]
    if opt_lokasi != "Semua":
        df_filtered = df_filtered[df_filtered['Lokasi_Rak'] == opt_lokasi]
    if opt_progres != "Semua":
        df_filtered = df_filtered[df_filtered['Status_Baca'] == opt_progres]
    if opt_kondisi != "Semua":
        df_filtered = df_filtered[df_filtered['Kondisi'] == opt_kondisi]

    # --- LIST BUKU ---
    st.subheader(f"{len(df_filtered)}")
    
    icon_book = get_icon("location") # Atau sesuaikan key icon buku kamu
    
    with st.container(border=True):
        for idx, row in df_filtered.iterrows():
            judul = row.get("Judul", "-")
            penulis = row.get("Penulis", "-")
            tahun = row.get("Tahun", "-")
            genre = row.get("Genre", "-")
            lokasi = row.get("Lokasi_Rak", "-")
            status_baca = row.get("Status_Baca", "Belum dibaca")
            rating = row.get("Rating", "Belum dinilai")
            peminjam = row.get("Peminjam", "")
            
            # Format teks lokasi jika sedang dipinjam
            if str(row.get("Status_Pinjam", "")).lower() == "dipinjam" and peminjam:
                lokasi_str = f"Dipinjam {peminjam}"
            else:
                lokasi_str = lokasi

            # Format teks status kanan
            if rating and rating != "-":
                status_kanan = f"{status_baca} · {rating}/5 ›"
            else:
                status_kanan = f"{status_baca} · Belum dinilai ›"

            # Render item per baris
            c_icon, c_info, c_status = st.columns([0.5, 6, 2.5])
            
            with c_icon:
                st.markdown(f"<div style='background: #2D3748; padding: 10px; border-radius: 8px; text-align: center;'>📖</div>", unsafe_allow_html=True)
            
            with c_info:
                st.markdown(f"**{judul}**")
                st.caption(f"{penulis} · {tahun} · {genre} | Lokasi: {lokasi_str}")
                
            with c_status:
                st.markdown(f"<div style='text-align: right; color: #A0AEC0; font-size: 14px; padding-top: 10px;'>{status_kanan}</div>", unsafe_allow_html=True)
            
            if idx < len(df_filtered) - 1:
                st.divider()