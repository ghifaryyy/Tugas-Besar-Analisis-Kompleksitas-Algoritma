# =============================================================================
# TUGAS BESAR: Perbandingan Binary Search Iteratif vs Rekursif pada Linked List
# File: app.py (Aplikasi Streamlit)
# =============================================================================
# Kode algoritma ada di file tubes.py
# =============================================================================

import streamlit as st
import matplotlib.pyplot as plt
import time

# Import dari tubes.py
from tubes import (
    LinkedList,
    binary_search_iteratif,
    binary_search_rekursif_wrapper,
    buat_linked_list_terurut
)


# =============================================================================
# FUNGSI UNTUK MENGUKUR WAKTU
# =============================================================================

def ukur_waktu(fungsi, *args):
    waktu_mulai = time.perf_counter()
    hasil = fungsi(*args)
    waktu_selesai = time.perf_counter()
    return hasil, waktu_selesai - waktu_mulai


def benchmark(ukuran_list, jumlah_pengulangan=5):
    """
    Benchmark untuk berbagai ukuran linked list
    
    PERBAIKAN:
    - Test WORST CASE (elemen terakhir) supaya operasi maksimal
    - Jalankan beberapa kali dan ambil rata-rata untuk kurangi noise
    - Hasil lebih representatif untuk analisis kompleksitas
    """
    hasil = {
        "ukuran": [],
        "waktu_iteratif": [],
        "waktu_rekursif": [],
        "operasi_iteratif": [],
        "operasi_rekursif": []
    }
    
    for ukuran in ukuran_list:
        # Buat linked list terurut: 1, 2, 3, ..., ukuran
        linked_list = buat_linked_list_terurut(ukuran)
        
        # WORST CASE: Cari elemen TERAKHIR (butuh log n operasi)
        # Ini membuat binary search harus kerja maksimal
        nilai_dicari = ukuran  # Elemen terakhir
        
        # Jalankan beberapa kali untuk kurangi noise
        total_waktu_iter = 0
        total_waktu_rek = 0
        ops_iter = 0
        ops_rek = 0
        
        for _ in range(jumlah_pengulangan):
            # Ukur iteratif
            (idx, ops), waktu_iter = ukur_waktu(
                binary_search_iteratif, linked_list, nilai_dicari
            )
            total_waktu_iter += waktu_iter
            ops_iter = ops  # Operasi selalu sama untuk input yang sama
            
            # Ukur rekursif
            (idx, depth), waktu_rek = ukur_waktu(
                binary_search_rekursif_wrapper, linked_list, nilai_dicari
            )
            total_waktu_rek += waktu_rek
            ops_rek = depth
        
        # Rata-rata waktu
        hasil["ukuran"].append(ukuran)
        hasil["waktu_iteratif"].append(total_waktu_iter / jumlah_pengulangan)
        hasil["waktu_rekursif"].append(total_waktu_rek / jumlah_pengulangan)
        hasil["operasi_iteratif"].append(ops_iter)
        hasil["operasi_rekursif"].append(ops_rek)
    
    return hasil


# =============================================================================
# KONFIGURASI HALAMAN
# =============================================================================

st.set_page_config(
    page_title="Binary Search: Iteratif vs Rekursif",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Perbandingan Binary Search")
st.subheader("Iteratif vs Rekursif pada Linked List")

st.markdown("""
Aplikasi ini membandingkan dua metode Binary Search pada **Linked List**:
- **Iteratif**: Menggunakan loop `while`
- **Rekursif**: Fungsi yang memanggil dirinya sendiri
""")

st.divider()


# =============================================================================
# SIDEBAR - INPUT DATA
# =============================================================================

st.sidebar.header("⚙️ Pengaturan")

mode_input = st.sidebar.radio(
    "Pilih mode input:",
    ["Gunakan contoh data", "Input manual", "Generate otomatis"]
)

linked_list = None

if mode_input == "Gunakan contoh data":
    data_contoh = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    linked_list = LinkedList()
    for x in data_contoh:
        linked_list.tambah_node(x)
    st.sidebar.info(f"Data contoh: {data_contoh}")

elif mode_input == "Input manual":
    input_user = st.sidebar.text_input(
        "Masukkan angka (pisahkan dengan koma):",
        value="1, 3, 5, 7, 9, 11, 13, 15"
    )
    
    try:
        data = [int(x.strip()) for x in input_user.split(",")]
        data.sort()
        linked_list = LinkedList()
        for x in data:
            linked_list.tambah_node(x)
        st.sidebar.success(f"List terurut: {data}")
    except ValueError:
        st.sidebar.error("Input tidak valid!")

else:  # Generate otomatis
    jumlah_elemen = st.sidebar.slider(
        "Jumlah elemen:",
        min_value=10,
        max_value=1000,
        value=100,
        step=10
    )
    linked_list = buat_linked_list_terurut(jumlah_elemen)
    st.sidebar.info(f"Linked List: 1 sampai {jumlah_elemen}")

# Input nilai yang dicari
st.sidebar.divider()

if linked_list and linked_list.panjang > 0:
    nilai_dicari = st.sidebar.number_input(
        "Nilai yang dicari:",
        min_value=1,
        max_value=linked_list.panjang + 10,
        value=linked_list.panjang // 2
    )
else:
    nilai_dicari = 1


# =============================================================================
# KONTEN UTAMA
# =============================================================================

if linked_list is None or linked_list.panjang == 0:
    st.warning("Linked List kosong! Silakan masukkan data.")
    st.stop()

# Tampilkan linked list
st.subheader("📋 Data Linked List")
if linked_list.panjang <= 50:
    # Tampilkan isi linked list
    elemen = []
    node = linked_list.kepala
    while node:
        elemen.append(str(node.data))
        node = node.pointer_berikutnya
    st.code(" → ".join(elemen))
else:
    st.info(f"Linked List: 1 sampai {linked_list.panjang} ({linked_list.panjang} elemen)")

st.divider()


# =============================================================================
# PENCARIAN
# =============================================================================

if st.button("🔍 Mulai Pencarian", type="primary"):
    
    col1, col2 = st.columns(2)
    
    # ITERATIF
    with col1:
        st.subheader("⚡ ITERATIF")
        
        (index, operasi), waktu = ukur_waktu(
            binary_search_iteratif, linked_list, nilai_dicari
        )
        
        if index != -1:
            st.success(f"✓ Ditemukan di index {index}")
        else:
            st.error(f"✗ Tidak ditemukan")
        
        st.metric("Jumlah Iterasi", operasi)
        st.metric("Waktu", f"{waktu:.6f} detik")
    
    # REKURSIF
    with col2:
        st.subheader("🔄 REKURSIF")
        
        (index, kedalaman), waktu = ukur_waktu(
            binary_search_rekursif_wrapper, linked_list, nilai_dicari
        )
        
        if index != -1:
            st.success(f"✓ Ditemukan di index {index}")
        else:
            st.error(f"✗ Tidak ditemukan")
        
        st.metric("Kedalaman Rekursi", kedalaman)
        st.metric("Waktu", f"{waktu:.6f} detik")


# =============================================================================
# BENCHMARK
# =============================================================================

st.divider()
st.subheader("📊 Benchmark Running Time")

st.markdown("""
Grafik perbandingan waktu eksekusi untuk berbagai ukuran linked list.
Sesuai dengan requirement tugas besar: ukuran 1, 10, 100, 1000, dll.
""")

if st.button("📈 Jalankan Benchmark"):
    
    ukuran_list = [10, 50, 100, 200, 300, 500, 750, 1000]
    
    with st.spinner("Menjalankan benchmark..."):
        hasil = benchmark(ukuran_list)
    
    st.success("Benchmark selesai!")
    
    # GRAFIK WAKTU
    st.subheader("Grafik Waktu Eksekusi")
    
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    
    waktu_iter_ms = [w * 1000 for w in hasil["waktu_iteratif"]]
    waktu_rek_ms = [w * 1000 for w in hasil["waktu_rekursif"]]
    
    ax1.plot(hasil["ukuran"], waktu_iter_ms, 'b-o', label='Iteratif', linewidth=2)
    ax1.plot(hasil["ukuran"], waktu_rek_ms, 'r-s', label='Rekursif', linewidth=2)
    
    ax1.set_xlabel('Ukuran Linked List (n)')
    ax1.set_ylabel('Waktu (milidetik)')
    ax1.set_title('Perbandingan Waktu Eksekusi pada Linked List')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    st.pyplot(fig1)
    
    # GRAFIK OPERASI
    st.subheader("Grafik Jumlah Operasi")
    
    # Catatan: Iteratif dan Rekursif punya operasi yang SAMA
    # Ini menunjukkan kedua algoritma punya kompleksitas operasi yang sama
    st.info("💡 **Catatan:** Garis Iteratif dan Rekursif berimpit karena jumlah operasinya **sama persis** (keduanya O(log n))")
    
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    
    # Tambah sedikit offset supaya garis terlihat
    ops_iter_offset = [x - 0.1 for x in hasil["operasi_iteratif"]]
    ops_rek_offset = [x + 0.1 for x in hasil["operasi_rekursif"]]
    
    ax2.plot(hasil["ukuran"], ops_iter_offset, 'b-o', 
             label='Iteratif', linewidth=2, markersize=8)
    ax2.plot(hasil["ukuran"], ops_rek_offset, 'r--s', 
             label='Rekursif', linewidth=2, markersize=8)
    
    ax2.set_xlabel('Ukuran Linked List (n)')
    ax2.set_ylabel('Jumlah Operasi')
    ax2.set_title('Perbandingan Jumlah Operasi (Keduanya O(log n))')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    st.pyplot(fig2)
    
    # TABEL
    st.subheader("Tabel Hasil Benchmark")
    
    import pandas as pd
    df = pd.DataFrame({
        "Ukuran": hasil["ukuran"],
        "Waktu Iteratif (ms)": [f"{w:.4f}" for w in waktu_iter_ms],
        "Waktu Rekursif (ms)": [f"{w:.4f}" for w in waktu_rek_ms],
        "Operasi Iteratif": hasil["operasi_iteratif"],
        "Operasi Rekursif": hasil["operasi_rekursif"]
    })
    
    st.dataframe(df, use_container_width=True)


# =============================================================================
# ANALISIS KOMPLEKSITAS
# =============================================================================

st.divider()
st.subheader("📚 Analisis Kompleksitas")

st.markdown("""
### Tabel Perbandingan Kompleksitas

| Kasus (Case) | Binary Search Iteratif | Binary Search Rekursif |
|--------------|------------------------|------------------------|
| **Best Case** | O(n) | O(n) |
| **Average Case** | O(n log n) | O(n) |
| **Worst Case** | O(n log n) | O(n) |
| **Kompleksitas Ruang** | O(1) | O(log n) |
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📘 Analisis Iteratif
    
    **Best Case:**
    ```
    T(n) = n/2 → T(n) ∈ O(n)
    ```
    Elemen ditemukan di posisi tengah pertama kali.
    
    **Average Case:**
    ```
    T(n) ≈ (n/2) × (log n / 2) = ¼ n log n
    T(n) ∈ O(n log n)
    ```
    
    **Worst Case:**
    ```
    T(n) = n × Σ(1) dari i=1 sampai log n
    T(n) = n × log n → T(n) ∈ O(n log n)
    ```
    """)

with col2:
    st.markdown("""
    ### 📗 Analisis Rekursif
    
    **Relasi Rekurensi:**
    ```
    T(n) = 1,           jika n = 1
    T(n) = T(n/2) + n,  jika n > 1
    ```
    
    **1. Peubah Variabel:**
    ```
    n = 2ᵏ → k = log₂ n
    T(2ᵏ) = T(2ᵏ⁻¹) + 2ᵏ
    ```
    
    **2. Persamaan Rekurensi:**
    ```
    aₖ - aₖ₋₁ = 2ᵏ
    Homogen: aₖ - aₖ₋₁ = 0
    Non-homogen: f(k) = 2ᵏ
    ```
    
    **3. Persamaan Karakteristik:**
    ```
    (a₀rᵏ + a₁rᵏ⁻¹ + ...)(r - b)^(d+1) = 0
    (r - 1)(r - 2) = 0
    r₁ = 1, r₂ = 2
    ```
    
    **4. Solusi Umum:**
    ```
    aₖ = c₁r₁ᵏ + c₂r₂ᵏ
    aₖ = c₁(1)ᵏ + c₂(2)ᵏ
    
    Syarat awal:
    1 = c₁(1) + c₂(1) → c₁ + c₂ = 1
    3 = c₁(1) + c₂(2) → c₁ + 2c₂ = 3
    
    Hasil: c₁ = -1, c₂ = 2
    ```
    
    **5. Solusi Khusus:**
    ```
    aₖ = c₁(1)ᵏ + c₂(2)ᵏ
    aₖ = (-1)·1 + (2)·2ᵏ
    aₖ = 2ᵏ⁺¹ - 1
    ```
    
    **6. Hasil Akhir:**
    ```
    T(n) = 2^(log₂n+1) - 1
    T(n) = 2(2^log₂n) - 1
    T(n) = 2n - 1
    T(n) ∈ O(n)
    ```
    Berlaku untuk **semua kasus**.
    """)

st.markdown("""
---

### Kesimpulan

**Catatan Penting:**
- Pada **Array**, Binary Search = O(log n) karena akses index O(1)
- Pada **Linked List**, Binary Search lebih lambat karena akses index = O(n)
- **Rekursif** memiliki kompleksitas waktu O(n) untuk semua kasus (berdasarkan analisis persamaan karakteristik: T(n) = 2n - 1)
- **Iteratif** memiliki kompleksitas O(n) pada best case, O(n log n) pada average/worst case
- Rekursif membutuhkan **memori tambahan O(log n)** untuk call stack
- **Trade-off:** Pilih Iteratif jika memori terbatas, pilih Rekursif jika butuh waktu konsisten
""")
