import streamlit as st

def render_right_column(buku):
    sinopsis = buku.get("Sinopsis", "Belum ada sinopsis.")
    review = buku.get("Review", "Belum ada ulasan.")
    progress_hlm = int(buku.get("Progress_Halaman", 0))
    total_hlm = int(buku.get("Total_Halaman", 1))
    persen = min(int((progress_hlm / total_hlm) * 100), 100) if total_hlm > 0 else 0

    # 1. Progres Membaca
    with st.container(border=True):
        st.markdown("<h4 style='color:#2D3748;'>Progres Membaca Pribadi</h4>", unsafe_allow_html=True)
        st.progress(persen / 100, text=f"{persen}% selesai ({progress_hlm} / {total_hlm} halaman)")
        
        st.write("")
        col_p1, col_p2 = st.columns([3, 1])
        col_p1.markdown("<span style='color:#718096;'>Sesi baca terakhir: Terbaru</span>", unsafe_allow_html=True)
        if col_p2.button("Update Halaman", use_container_width=True):
            st.toast("Halaman berhasil diperbarui!")

    # 2. Sinopsis Buku
    with st.container(border=True):
        st.markdown("<h4 style='color:#2D3748;'>Sinopsis Buku</h4>", unsafe_allow_html=True)
        st.write(sinopsis)

    # 3. Catatan & Ulasan Pribadi
    rating = buku.get("Rating", "5.0")

    with st.container(border=True):
        st.markdown(f'<h4 style="color:#2D3748;">Catatan & Ulasan Pribadi <span class="rating-badge">Rating Pribadi: ★ {rating}/5</span></h4>', unsafe_allow_html=True)
        st.info(f'"{review}"')
        ...
        