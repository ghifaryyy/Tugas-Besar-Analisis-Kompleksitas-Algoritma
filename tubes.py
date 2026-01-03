# =============================================================================
# TUGAS BESAR: Perbandingan Binary Search Iteratif vs Rekursif pada Linked List
# =============================================================================

import time


# =============================================================================
# STRUKTUR DATA: NODE DAN LINKED LIST
# =============================================================================

class Node:
    """
    Node untuk Linked List
    Setiap node menyimpan data dan pointer ke node berikutnya
    """
    def __init__(self, data):
        self.data = data
        self.pointer_berikutnya = None


class LinkedList:
    """
    Linked List satu arah (Singly Linked List)
    """
    def __init__(self):
        self.kepala = None
        self.panjang = 0
    
    def tambah_node(self, data):
        """Menambahkan node baru di akhir linked list"""
        node_baru = Node(data)
        
        if self.kepala is None:
            self.kepala = node_baru
        else:
            current = self.kepala
            while current.pointer_berikutnya:
                current = current.pointer_berikutnya
            current.pointer_berikutnya = node_baru
        
        self.panjang += 1
    
    def ambil_node_pada_index(self, index):
        """
        Mengambil node pada index tertentu
        PENTING: Ini adalah operasi O(n) karena harus traversal dari kepala!
        """
        if index < 0 or index >= self.panjang:
            return None
        
        current = self.kepala
        for _ in range(index):
            current = current.pointer_berikutnya
        
        return current


# =============================================================================
# FUNGSI HELPER
# =============================================================================

def buat_linked_list_terurut(ukuran):
    """Membuat linked list dengan elemen 1, 2, 3, ..., ukuran"""
    ll = LinkedList()
    for i in range(1, ukuran + 1):
        ll.tambah_node(i)
    return ll


# =============================================================================
# ALGORITMA 1: BINARY SEARCH ITERATIF PADA LINKED LIST
# =============================================================================

def binary_search_iteratif(linked_list, nilai_dicari):
    """
    Binary Search Iteratif pada Linked List
    
    KOMPLEKSITAS:
    - Best Case: O(n) - traversal ke tengah saja
    - Average/Worst Case: O(n log n) - karena traversal dari kepala setiap iterasi
    - Ruang: O(1)
    """
    batas_kiri = 0
    batas_kanan = linked_list.panjang - 1
    jumlah_iterasi = 0
    
    while batas_kiri <= batas_kanan:
        jumlah_iterasi += 1
        
        # Hitung index tengah
        index_tengah = (batas_kiri + batas_kanan) // 2
        
        # TRAVERSAL: Ambil node di index tengah - O(n)!
        node_tengah = linked_list.ambil_node_pada_index(index_tengah)
        nilai_tengah = node_tengah.data
        
        if nilai_tengah == nilai_dicari:
            return index_tengah, jumlah_iterasi
        elif nilai_tengah < nilai_dicari:
            batas_kiri = index_tengah + 1
        else:
            batas_kanan = index_tengah - 1
    
    return -1, jumlah_iterasi


# =============================================================================
# ALGORITMA 2: BINARY SEARCH REKURSIF PADA LINKED LIST
# =============================================================================

def binary_search_rekursif(linked_list, nilai_dicari, batas_kiri, batas_kanan, kedalaman=0):
    """
    Binary Search Rekursif pada Linked List
    
    KOMPLEKSITAS (berdasarkan persamaan karakteristik):
    - T(n) = T(n/2) + n
    - Solusi: T(n) = 2n - 1
    - Semua Case: O(n)
    - Ruang: O(log n) untuk call stack
    """
    kedalaman += 1
    
    # Base case: tidak ditemukan
    if batas_kiri > batas_kanan:
        return -1, kedalaman
    
    # Hitung index tengah
    index_tengah = (batas_kiri + batas_kanan) // 2
    
    # TRAVERSAL: Ambil node di index tengah - O(n)!
    node_tengah = linked_list.ambil_node_pada_index(index_tengah)
    nilai_tengah = node_tengah.data
    
    # Base case: ditemukan
    if nilai_tengah == nilai_dicari:
        return index_tengah, kedalaman
    
    # Recursive case
    elif nilai_tengah < nilai_dicari:
        return binary_search_rekursif(
            linked_list, nilai_dicari, 
            index_tengah + 1, batas_kanan, 
            kedalaman
        )
    else:
        return binary_search_rekursif(
            linked_list, nilai_dicari, 
            batas_kiri, index_tengah - 1, 
            kedalaman
        )


def binary_search_rekursif_wrapper(linked_list, nilai_dicari):
    """Wrapper untuk memudahkan pemanggilan"""
    return binary_search_rekursif(
        linked_list, nilai_dicari,
        0, linked_list.panjang - 1
    )


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("DEMO: Binary Search pada Linked List")
    print("=" * 60)
    
    # Buat linked list
    ll = buat_linked_list_terurut(15)
    nilai_dicari = 7
    
    print(f"\nLinked List: 1 sampai 15")
    print(f"Nilai dicari: {nilai_dicari}")
    
    # Test Iteratif
    print("\n--- ITERATIF ---")
    index, ops = binary_search_iteratif(ll, nilai_dicari)
    print(f"Index: {index}, Jumlah iterasi: {ops}")
    
    # Test Rekursif
    print("\n--- REKURSIF ---")
    index, depth = binary_search_rekursif_wrapper(ll, nilai_dicari)
    print(f"Index: {index}, Kedalaman rekursi: {depth}")
