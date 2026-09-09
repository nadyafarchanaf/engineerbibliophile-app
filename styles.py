import streamlit as st

def load_css():
    st.markdown("""
    <style>
        /* 1. Background Utama (Soft Cream) */
        .stApp {
            background-color: #F8F5F0 !important;
            color: #2D3748 !important;
        }
        
        /* 2. Style Kartu/Container Putih Bersih */
        .custom-card-box {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.03);
        }

        /* 3. Perbaiki Tombol Bawaan Streamlit */
        .stButton > button {
            background-color: #FFFFFF !important;
            color: #2D3748 !important;
            border: 1px solid #CBD5E0 !important;
            border-radius: 8px !important;
            font-weight: 500 !important;
        }
        .stButton > button:hover {
            background-color: #EDF2F7 !important;
            border-color: #A0AEC0 !important;
        }
        
        /* Tombol Utama (Primary) */
        .stButton > button[kind="primary"] {
            background-color: #E53E3E !important;
            color: #FFFFFF !important;
            border: none !important;
        }

        /* 4. Perbaiki Text Area & Input Box */
        .stTextArea textarea {
            background-color: #FFFFFF !important;
            color: #2D3748 !important;
            border: 1px solid #CBD5E0 !important;
            border-radius: 8px !important;
        }

        /* 5. Teks Muted & Badges */
        .text-dark {
            color: #2D3748 !important;
        }
        .text-muted-custom {
            color: #718096 !important;
            font-size: 14px;
        }
        .rating-badge {
            background-color: #FEFCBF !important;
            color: #744210 !important;
            border: 1px solid #FEEBC8 !important;
            padding: 2px 8px;
            border-radius: 8px;
            font-size: 12px;
            float: right;
        }
    </style>
    """, unsafe_allow_html=True)

    # styles.py

SVG_PATHS = {
    "location": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "barcode": '<path d="M3 5v14"/><path d="M8 5v14"/><path d="M12 5v14"/><path d="M17 5v14"/><path d="M21 5v14"/>',
    "calendar": '<rect width="18" height="18" x="3" y="4" rx="2" ry="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/>',
    "store": '<path d="m2 7 1 12a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2l1-12"/><path d="M2 7h20"/><path d="M16 11a4 4 0 0 1-8 0"/>'
}

def get_icon(name, color="#7D9376", size=20):
    path = SVG_PATHS.get(name, "")
    style = "vertical-align: middle; margin-right: 8px;"
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="{style}">{path}</svg>'