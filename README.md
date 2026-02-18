# Analisis Perbandingan Efisiensi: Binary Search Iteratif vs Rekursif pada Linked List

Proyek ini bertujuan untuk menganalisis dan membandingkan kinerja algoritma **Binary Search** versi iteratif dan rekursif ketika diterapkan pada struktur data **Linked List** terurut. Fokus utama analisis ini adalah melihat bagaimana karakteristik akses sekuensial pada Linked List memengaruhi kompleksitas waktu ($T(n)$) dan penggunaan memori ($O(1)$ vs $O(\log n)$).

## 🧐 Latar Belakang
Binary Search dikenal sangat optimal ($O(\log n)$) pada Array karena fitur *random access*. Namun, pada Linked List, setiap pengambilan elemen tengah memerlukan proses **traversal** dari node awal, yang secara signifikan mengubah efisiensi algoritma tersebut.

## 🛠️ Tech Stack & Metode
* **Bahasa Pemrograman:** Python
* **Struktur Data:** Singly Linked List (Terurut menaik)
* **Metode Analisis:** Perhitungan matematis (Relasi Rekurensi & Persamaan Karakteristik) dan pengujian empiris (Grafik Waktu Eksekusi).

## 🚀 Perbandingan Karakteristik Teknis
Berdasarkan hasil analisis, berikut adalah perbandingan kompleksitas kedua metode pada Linked List:

<img width="920" height="375" alt="image" src="https://github.com/user-attachments/assets/e36c0e47-0ed4-4faa-95d5-8aacee7dc455" />


## 📊 Temuan Utama
1. **Dominasi Traversal:** Meskipun jumlah pembelahan ruang pencarian bersifat logaritmik ($O(\log n)$), waktu eksekusi tetap meningkat secara linear karena biaya utama berasal dari proses traversal node untuk menemukan elemen tengah.
2. **Efisiensi Waktu:** Berdasarkan analisis persamaan karakteristik $T(n) = 2n - 1$, versi **Rekursif** memiliki kompleksitas waktu $O(n)$ yang lebih konsisten untuk semua kasus dibandingkan versi Iteratif.
3. **Efisiensi Memori:** Versi **Iteratif** jauh lebih unggul dalam penggunaan memori ($O(1)$) karena hanya menggunakan variabel lokal, sedangkan versi Rekursif memberikan beban tambahan pada *call stack* sebesar $O(\log n)$.

## 💡 Kesimpulan
Pemilihan antara kedua metode pada Linked List bergantung pada prioritas:
* Gunakan **Iteratif** jika ingin menghemat memori.
* Gunakan **Rekursif** jika memprioritaskan konsistensi waktu eksekusi.
* Namun, secara umum Binary Search tetap kurang optimal pada Linked List jika dibandingkan dengan Array.

## 👥 Tim Penyusun (DS-48-03)
Mahasiswa S-1 Sains Data, Universitas Telkom:
* **Ghifary Wibisono** (103052400016)
* **Prayata Yasinkha Adnien** (103052400060)
* **Luthfia Maulidya Izzati** (103052400066)

---
*Proyek ini merupakan bagian dari Tugas Besar Mata Kuliah Analisis Kompleksitas Algoritma (AKA) 2025.*
