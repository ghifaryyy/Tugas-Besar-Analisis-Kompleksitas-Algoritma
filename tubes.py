# =============================================================================
# TUGAS BESAR: Perbandingan Binary Search Iteratif vs Rekursif pada Linked List
# =============================================================================

# =============================================================================
# BAGIAN 1: STRUKTUR DATA LINKED LIST
# =============================================================================

class Node:
    """
    Kelas Node: Representasi satu elemen dalam Linked List
    
    Setiap node menyimpan:
    - data: nilai yang disimpan
    - pointer_berikutnya: referensi ke node selanjutnya
    """
    def __init__(self, data):
        self.data = data
        self.pointer_berikutnya = None  # Awalnya tidak menunjuk kemana-mana


class LinkedList:
    """
    Kelas LinkedList: Struktur data Linked List
    
    Menyimpan:
    - kepala: pointer ke node pertama
    - panjang: jumlah total node dalam list
    """
    def __init__(self):
        self.kepala = None  # List kosong, tidak ada node
        self.panjang = 0
    
    def tambah_node(self, data):
        """
        Menambahkan node baru di akhir linked list
        
        Langkah:
        1. Buat node baru
        2. Jika list kosong, node baru jadi kepala
        3. Jika tidak, traversal ke akhir lalu sambungkan
        """
        node_baru = Node(data)
        
        # Kasus 1: List masih kosong
        if self.kepala is None:
            self.kepala = node_baru
            self.panjang += 1
            return
        
        # Kasus 2: List sudah ada isinya, traversal ke akhir
        node_saat_ini = self.kepala
        while node_saat_ini.pointer_berikutnya is not None:
            node_saat_ini = node_saat_ini.pointer_berikutnya
        
        # Sambungkan node baru di akhir
        node_saat_ini.pointer_berikutnya = node_baru
        self.panjang += 1
    
    def ambil_node_pada_index(self, index):
        """
        Mengambil node pada index tertentu
        
        PENTING: Di Linked List, kita HARUS traversal dari kepala!
        Tidak bisa langsung akses seperti array.
        
        Kompleksitas: O(n) - harus jalan satu per satu
        """
        if index < 0 or index >= self.panjang:
            return None
        
        node_saat_ini = self.kepala
        for langkah in range(index):
            node_saat_ini = node_saat_ini.pointer_berikutnya
        
        return node_saat_ini
    
    def tampilkan_list(self):
        """Menampilkan semua elemen dalam linked list"""
        if self.kepala is None:
            print("List kosong")
            return
        
        node_saat_ini = self.kepala
        elemen_list = []
        while node_saat_ini is not None:
            elemen_list.append(str(node_saat_ini.data))
            node_saat_ini = node_saat_ini.pointer_berikutnya
        
        print(" -> ".join(elemen_list))


# =============================================================================
# BAGIAN 2: ALGORITMA BINARY SEARCH ITERATIF
# =============================================================================

def binary_search_iteratif(linked_list, nilai_dicari):
    """
    Binary Search dengan pendekatan ITERATIF (menggunakan loop while)
    
    PRASYARAT: Linked List harus sudah TERURUT dari kecil ke besar!
    
    CARA KERJA:
    1. Tentukan batas kiri (index 0) dan batas kanan (index terakhir)
    2. Selama batas kiri <= batas kanan:
       a. Hitung index tengah
       b. Ambil nilai di index tengah (PERLU TRAVERSAL!)
       c. Bandingkan dengan nilai yang dicari
       d. Jika sama → ketemu!
       e. Jika nilai tengah < nilai dicari → cari di bagian kanan
       f. Jika nilai tengah > nilai dicari → cari di bagian kiri
    3. Jika loop selesai tanpa ketemu → nilai tidak ada
    
    KOMPLEKSITAS WAKTU: O(n log n)
    - Binary Search biasa: O(log n) iterasi
    - Tapi setiap iterasi perlu traversal ke tengah: O(n)
    - Total: O(n) × O(log n) = O(n log n)
    
    KOMPLEKSITAS RUANG: O(1) - hanya pakai variabel lokal
    
    Parameter:
    - linked_list: objek LinkedList yang sudah terurut
    - nilai_dicari: nilai yang ingin dicari
    
    Return:
    - index jika ditemukan
    - -1 jika tidak ditemukan
    """
    
    # Inisialisasi batas pencarian
    batas_kiri = 0
    batas_kanan = linked_list.panjang - 1
    
    # Counter untuk menghitung jumlah iterasi (untuk analisis)
    jumlah_iterasi = 0
    
    # Loop utama Binary Search
    while batas_kiri <= batas_kanan:
        jumlah_iterasi += 1
        
        # Hitung index tengah
        index_tengah = (batas_kiri + batas_kanan) // 2
        
        # TRAVERSAL: Ambil node di index tengah
        # INI YANG MEMBUAT KOMPLEKSITAS MENJADI O(n log n)!
        node_tengah = linked_list.ambil_node_pada_index(index_tengah)
        nilai_tengah = node_tengah.data
        
        # Bandingkan nilai
        if nilai_tengah == nilai_dicari:
            # KETEMU! Return index-nya
            return index_tengah, jumlah_iterasi
        
        elif nilai_tengah < nilai_dicari:
            # Nilai yang dicari lebih besar
            # Berarti ada di BAGIAN KANAN, geser batas kiri
            batas_kiri = index_tengah + 1
        
        else:  # nilai_tengah > nilai_dicari
            # Nilai yang dicari lebih kecil
            # Berarti ada di BAGIAN KIRI, geser batas kanan
            batas_kanan = index_tengah - 1
    
    # Tidak ditemukan
    return -1, jumlah_iterasi


# =============================================================================
# BAGIAN 3: ALGORITMA BINARY SEARCH REKURSIF
# =============================================================================

def binary_search_rekursif(linked_list, nilai_dicari, batas_kiri, batas_kanan, kedalaman_rekursi=0):
    """
    Binary Search dengan pendekatan REKURSIF (fungsi memanggil dirinya sendiri)
    
    PRASYARAT: Linked List harus sudah TERURUT dari kecil ke besar!
    
    CARA KERJA:
    1. Base Case 1: Jika batas kiri > batas kanan → tidak ditemukan
    2. Hitung index tengah
    3. Ambil nilai di index tengah (PERLU TRAVERSAL!)
    4. Base Case 2: Jika nilai tengah == nilai dicari → ketemu!
    5. Recursive Case:
       - Jika nilai tengah < nilai dicari → rekursi ke bagian kanan
       - Jika nilai tengah > nilai dicari → rekursi ke bagian kiri
    
    KOMPLEKSITAS WAKTU: O(n log n) - sama dengan iteratif
    
    KOMPLEKSITAS RUANG: O(log n)
    - Setiap pemanggilan rekursif menambah call stack
    - Maksimal kedalaman rekursi = log n
    
    Parameter:
    - linked_list: objek LinkedList yang sudah terurut
    - nilai_dicari: nilai yang ingin dicari
    - batas_kiri: index batas kiri pencarian
    - batas_kanan: index batas kanan pencarian
    - kedalaman_rekursi: untuk tracking jumlah pemanggilan rekursif
    
    Return:
    - (index, kedalaman) jika ditemukan
    - (-1, kedalaman) jika tidak ditemukan
    """
    
    kedalaman_rekursi += 1
    
    # BASE CASE 1: Batas sudah tidak valid
    if batas_kiri > batas_kanan:
        return -1, kedalaman_rekursi
    
    # Hitung index tengah
    index_tengah = (batas_kiri + batas_kanan) // 2
    
    # TRAVERSAL: Ambil node di index tengah
    # INI YANG MEMBUAT KOMPLEKSITAS MENJADI O(n log n)!
    node_tengah = linked_list.ambil_node_pada_index(index_tengah)
    nilai_tengah = node_tengah.data
    
    # BASE CASE 2: Nilai ditemukan!
    if nilai_tengah == nilai_dicari:
        return index_tengah, kedalaman_rekursi
    
    # RECURSIVE CASE
    elif nilai_tengah < nilai_dicari:
        # Rekursi ke BAGIAN KANAN
        return binary_search_rekursif(
            linked_list, 
            nilai_dicari, 
            index_tengah + 1,  # Batas kiri baru = tengah + 1
            batas_kanan,
            kedalaman_rekursi
        )
    
    else:  # nilai_tengah > nilai_dicari
        # Rekursi ke BAGIAN KIRI
        return binary_search_rekursif(
            linked_list, 
            nilai_dicari, 
            batas_kiri,
            index_tengah - 1,  # Batas kanan baru = tengah - 1
            kedalaman_rekursi
        )


def binary_search_rekursif_wrapper(linked_list, nilai_dicari):
    """
    Wrapper function untuk memudahkan pemanggilan Binary Search Rekursif
    
    User tidak perlu input batas_kiri dan batas_kanan secara manual
    """
    return binary_search_rekursif(
        linked_list,
        nilai_dicari,
        batas_kiri=0,
        batas_kanan=linked_list.panjang - 1
    )


# =============================================================================
# BAGIAN 4: FUNGSI UNTUK TESTING DAN DEMO
# =============================================================================

def buat_linked_list_terurut(jumlah_elemen):
    """
    Membuat Linked List yang sudah terurut dengan jumlah elemen tertentu
    Nilai: 1, 2, 3, ..., jumlah_elemen
    """
    linked_list_baru = LinkedList()
    for nilai in range(1, jumlah_elemen + 1):
        linked_list_baru.tambah_node(nilai)
    return linked_list_baru


def demo_binary_search():
    """
    Demonstrasi penggunaan Binary Search Iteratif dan Rekursif
    """
    print("=" * 60)
    print("DEMO: Binary Search pada Linked List")
    print("=" * 60)
    
    # Buat linked list dengan 10 elemen
    print("\n1. Membuat Linked List terurut dengan 10 elemen...")
    daftar = buat_linked_list_terurut(10)
    print("   Isi Linked List: ", end="")
    daftar.tampilkan_list()
    
    # Test Binary Search Iteratif
    print("\n2. Binary Search ITERATIF")
    print("-" * 40)
    
    nilai_target = 7
    print(f"   Mencari nilai: {nilai_target}")
    
    hasil_index, jumlah_iterasi = binary_search_iteratif(daftar, nilai_target)
    if hasil_index != -1:
        print(f"   ✓ Ditemukan di index: {hasil_index}")
    else:
        print(f"   ✗ Tidak ditemukan")
    print(f"   Jumlah iterasi: {jumlah_iterasi}")
    
    # Test Binary Search Rekursif
    print("\n3. Binary Search REKURSIF")
    print("-" * 40)
    
    print(f"   Mencari nilai: {nilai_target}")
    
    hasil_index, kedalaman = binary_search_rekursif_wrapper(daftar, nilai_target)
    if hasil_index != -1:
        print(f"   ✓ Ditemukan di index: {hasil_index}")
    else:
        print(f"   ✗ Tidak ditemukan")
    print(f"   Kedalaman rekursi: {kedalaman}")
    
    # Test dengan nilai yang tidak ada
    print("\n4. Test dengan nilai yang TIDAK ADA dalam list")
    print("-" * 40)
    
    nilai_tidak_ada = 15
    print(f"   Mencari nilai: {nilai_tidak_ada}")
    
    hasil_iteratif, _ = binary_search_iteratif(daftar, nilai_tidak_ada)
    hasil_rekursif, _ = binary_search_rekursif_wrapper(daftar, nilai_tidak_ada)
    
    print(f"   Iteratif: {'Ditemukan' if hasil_iteratif != -1 else 'Tidak ditemukan'}")
    print(f"   Rekursif: {'Ditemukan' if hasil_rekursif != -1 else 'Tidak ditemukan'}")
    
    print("\n" + "=" * 60)
    print("Demo selesai!")
    print("=" * 60)


# =============================================================================
# MAIN: Jalankan demo jika file dieksekusi langsung
# =============================================================================

if __name__ == "__main__":
    demo_binary_search()
