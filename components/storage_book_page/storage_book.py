import streamlit as st
import pandas as pd

def render_storage_page(df_buku):
    # --- HEADER ---
    col_header, col_btn = st.columns([4, 1])
    with col_header:
        st.title("Tempat Penyimpanan Buku")
    with col_btn:
        st.write("")
        st.button("+ Tambah Lokasi Baru", type="primary", use_container_width=True)

    # --- BANNER RINGKASAN ---
    total_rak = df_buku["Lokasi_Rak"].nunique() if "Lokasi_Rak" in df_buku else 0
    total_di_rak = len(df_buku[df_buku["Status_Pinjam"].str.lower() != "dipinjam"]) if "Status_Pinjam" in df_buku else 0
    total_dipinjam = len(df_buku[df_buku["Status_Pinjam"].str.lower() == "dipinjam"]) if "Status_Pinjam" in df_buku else 0

    with st.container(border=True):
        c1, c2, c3 = st.columns([2.5, 1, 1])
        with c1:
            st.markdown(f"🏛️ **{total_rak} Titik Penyimpanan Fisik Aktif**")
            st.caption("Semua rak, ambalan dinding, dan kotak arsip bebas rayap terpantau rapi.")
        with c2:
            st.markdown(f"<div style='background:#1A202C; padding:8px 12px; border-radius:6px; font-size:13px;'>📚 Total di rak: <b>{total_di_rak} buku</b></div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div style='background:#1A202C; padding:8px 12px; border-radius:6px; font-size:13px;'>🚚 Di luar (dipinjam): <b>{total_dipinjam} buku</b></div>", unsafe_allow_html=True)

    st.write("")

    # --- LAYOUT 2 KOLOM ---
    left_col, right_col = st.columns([1.2, 1.8])

    # 1. KOLOM KIRI: DAFTAR RAK / LEMARI
    with left_col:
        st.subheader("Daftar Rak & Lemari Penyimpanan")
        
        # Kelompokkan data per Lokasi_Rak
        if "Lokasi_Rak" in df_buku and not df_buku.empty:
            rak_groups = df_buku.groupby("Lokasi_Rak")
            
            for nama_rak, group in rak_groups:
                if not nama_rak or nama_rak == "-":
                    continue
                    
                jumlah_eksemplar = len(group)
                
                with st.container(border=True):
                    # Header Card Rak
                    rk1, rk2 = st.columns([2, 1])
                    rk1.caption("ZONA PENYIMPANAN")
                    rk2.markdown(f"<div style='text-align:right;'><span style='background:#2D3748; padding:2px 8px; border-radius:10px; font-size:11px; color:#E2E8F0;'>{jumlah_eksemplar} Eksemplar</span></div>", unsafe_allow_html=True)
                    
                    st.markdown(f"#### {nama_rak}")
                    st.caption("Lokasi penyimpanan fisik aktif.")
                    st.divider()
                    
                    # Footer Card Rak
                    rf1, rf2 = st.columns([1.5, 1])
                    rf1.caption("Status fisik: **Bagus & Kering**")
                    rf2.markdown("<div style='text-align:right; font-size:12px; color:#A0AEC0;'>Kelola & Cek Isi →</div>", unsafe_allow_html=True)

    # 2. KOLOM KANAN: POSISI BUKU SAAT INI (TABLE)
    with right_col:
        st.subheader("Posisi Buku Saat Ini")
        
        # Siapkan data tabel
        data_tabel = []
        for _, row in df_buku.iterrows():
            judul = row.get("Judul", "-")
            penulis = row.get("Penulis", "-")
            lokasi = row.get("Lokasi_Rak", "-")
            kondisi = row.get("Kondisi", "Baik")
            status_pinjam = str(row.get("Status_Pinjam", "")).lower()
            peminjam = row.get("Peminjam", "")

            # Tempat/Posisi menyesuaikan status pinjam
            if status_pinjam == "dipinjam" and peminjam:
                posisi = f"Dipinjam {peminjam}"
            else:
                posisi = lokasi

            data_tabel.append({
                "Judul Buku": judul,
                "Penulis": penulis,
                "Tempat / Posisi": posisi,
                "Status Fisik": kondisi
            })

        df_tabel = pd.DataFrame(data_tabel)
        
        # Display Table Custom HTML
        with st.container(border=True):
            st.dataframe(
                df_tabel,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Judul Buku": st.column_config.TextColumn(width="medium"),
                    "Penulis": st.column_config.TextColumn(width="small"),
                    "Tempat / Posisi": st.column_config.TextColumn(width="medium"),
                    "Status Fisik": st.column_config.TextColumn(width="small")
                }
            )