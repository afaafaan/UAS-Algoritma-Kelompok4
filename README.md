# 🍔 Sistem Manajemen Restoran XYZ

**Proyek Ujian Akhir Semester (UAS) - Mata Kuliah Algoritma & Struktur Data**  
*Implementasi Struktur Data Mandiri pada Studi Kasus Nyata Restoran & Kasir.*

---

## 👥 Anggota Kelompok 4
* **Abyan Farisa** (NIM: K3525018)
* **Sekar Hanny Keisha Azahra** (NIM: K3525041)
* **'Azzam Tsabitul Jamil** (NIM: K3523001) 

**Dosen Pengampu:** Yusfia Hafid Aristyagama S.T, M.T.  
**Program Studi:** S1 Pendidikan Teknik Informatika dan Komputer  
**Fakultas:** Keguruan dan Ilmu Pendidikan, Universitas Sebelas Maret (UNS)  
**Tahun:** 2026

---

## 🎯 Tujuan Proyek
1. **Menyelesaikan Masalah Aliran Pesanan Restoran:** Memodelkan alur kerja layanan kuliner mulai dari pemesanan kasir (FIFO), penyusunan menu (Hierarkis), prioritas dapur (Antrean berprioritas), hingga pencatatan riwayat nota selesai (LIFO).
2. **Implementasi Struktur Data Mandiri:** Membangun seluruh struktur data utama dari nol (murni manual) tanpa menggunakan library bawaan Python seperti `queue`, `collections.deque`, `heapq`, `PriorityQueue`, atau library binary tree pihak ketiga, guna mendalami logika algoritma dasar.
3. **Integrasi Sistem:** Menghubungkan keempat struktur data utama ke dalam satu alur bisnis restoran terintegrasi yang dijalankan berbasis Console CLI.

---

## 🗂️ Arsitektur Kode (MVC Pattern)
Sistem ini dirancang menggunakan konsep arsitektur **Model-View-Controller (MVC)** yang disederhanakan untuk memisahkan logika bisnis (services) dengan tampilan antarmuka (view).

```
UAS-Algoritma-Kelompok4/
│
├── main.py                    # Entry point program & inisialisasi menu awal
├── README.md                  # Dokumentasi proyek
│
├── models/
│   └── node_menu.py           # Model Node untuk representasi item menu dalam BST
│
├── services/
│   ├── bst_services.py        # Logika Binary Search Tree (BST) untuk daftar menu
│   ├── queue_services.py      # Logika Queue untuk antrean pesanan di kasir
│   ├── heap_service.py        # Logika Binary Heap untuk prioritas masakan di dapur
│   └── stack_services.py      # Logika Stack untuk riwayat pesanan selesai
│
└── views/
    └── kasir_view.py          # Antarmuka CLI dan logika pengendali input user
```

---

## ⚙️ Penjelasan Logika & Struktur Data

### 1. Manajemen Menu menggunakan Binary Search Tree (BST)
* **Konsep:** Digunakan untuk menyimpan daftar menu secara hierarkis dan teratur. Setiap node merepresentasikan satu menu makanan/minuman yang diatur berdasarkan urutan alfabetis nama menu.
* **Kelebihan:** Mempercepat pencarian menu dengan kompleksitas waktu rata-rata $O(\log n)$ dibanding menggunakan pencarian sekuensial list biasa $O(n)$. Menampilkan menu secara urut abjad dapat dilakukan secara efisien menggunakan metode **In-Order Traversal**.
* **Operasi Utama:** `insert`, `search`, `delete`, `inorder` (traversal), `get_height`, `count_nodes`.

### 2. Antrean Kasir menggunakan Queue (FIFO)
* **Konsep:** Digunakan untuk menampung antrean pesanan pelanggan di kasir dengan prinsip *First-In First-Out (FIFO)*. Pelanggan yang memesan terlebih dahulu wajib dilayani dan diproses ke dapur lebih awal.
* **Fitur VIP:** Mendukung penentuan pelanggan **VIP**. Ketika pesanan ditandai sebagai VIP, nama pesanan akan diawali dengan `"VIP "` (misal: `"VIP Nasi Goreng"`) dan dimasukkan ke dalam Queue antrean kasir dalam format objek dictionary.
* **Operasi Utama:** `enqueue` (menambahkan pesanan ke belakang antrean), `dequeue` (memanggil pesanan paling depan), `peek` (melihat pesanan berikutnya), `display` (menampilkan antrean kasir).

### 3. Prioritas Dapur menggunakan Binary Heap (Max-Heap)
* **Konsep:** Pesanan yang masuk ke dapur tidak selalu dimasak berdasarkan waktu kedatangan, melainkan berdasarkan tingkat kepentingan. Oleh karena itu digunakan **Max-Heap** untuk mengelola antrean dapur.
* **Skala Prioritas:**
  * **Prioritas 5 (Tertinggi):** Pesanan dengan status VIP (mengandung kata `"VIP"`).
  * **Prioritas 3:** Pesanan berupa minuman atau dessert (cepat saji).
  * **Prioritas 2:** Pesanan berupa makanan berat biasa.
  * **Prioritas 1 (Terendah):** Pesanan umum lainnya.
* **Kelebihan:** Elemen dengan prioritas tertinggi selalu berada di posisi root ($O(1)$) sehingga koki dapat langsung mengambil pesanan terpenting untuk dimasak lebih dulu. Penyesuaian heap (heapify) hanya memakan waktu $O(\log n)$.
* **Operasi Utama:** `insert`, `heapify_up`, `heapify_down`, `delete_root` / `extract_max`.

### 4. Riwayat Nota menggunakan Stack (LIFO)
* **Konsep:** Digunakan untuk menaruh riwayat pesanan yang sudah selesai dimasak dengan prinsip *Last-In First-Out (LIFO)*.
* **Kelebihan:** Memudahkan kasir dan koki melihat pesanan yang paling baru selesai dimasak berada di urutan paling atas untuk kemudahan pelacakan (*tracking*).
* **Operasi Utama:** `push` (menambahkan riwayat selesai ke atas tumpukan), `pop` (membatalkan/mengambil riwayat terakhir), `peek`, `display`.

---

## 🔁 Alur Proses Bisnis Integrasi
```
[Pelanggan Memesan] 
      │
      ▼
 [Daftar Menu BST] ───> Cari Validitas Menu & Tentukan VIP (y/n)
      │
      ▼
  [Queue Kasir] ──────> Antrean masuk berdasarkan waktu (FIFO)
      │ (Kirim ke Dapur / Dequeue)
      ▼
 [Max-Heap Dapur] ────> Diurutkan berdasarkan Prioritas (VIP > Minuman > Makanan)
      │ (Koki Selesai Memasak / Extract Max)
      ▼
  [Stack Riwayat] ────> Dicatat dalam tumpukan riwayat selesai (LIFO)
```

---

## 🚀 Langkah-Langkah Menjalankan Program

Sistem ini berbasis konsol CLI dan ditulis murni menggunakan Python Standard Library.

1. Buka Terminal, PowerShell, atau Command Prompt Anda.
2. Arahkan direktori (cd) ke folder proyek:
   ```bash
   cd "path/to/UAS-Algoritma-Kelompok4-2"
   ```
3. Jalankan aplikasi menggunakan perintah berikut:
   ```bash
   python main.py
   ```

### 💡 Mengatasi Masalah Emoji di Terminal Windows
Karena program ini menggunakan representasi emoji (`🍔`, `🍳`, `✅`, dll.) pada teks konsolnya, pada beberapa versi sistem Windows Anda mungkin mengalami `UnicodeEncodeError` jika terminal menggunakan encoding `cp1252`.
* **Untuk PowerShell:**
  Jalankan perintah ini sebelum menjalankan python:
  ```powershell
  $env:PYTHONUTF8=1
  python main.py
  ```
* **Untuk Command Prompt (CMD):**
  Jalankan perintah ini:
  ```cmd
  set PYTHONUTF8=1
  python main.py
  ```

---

## 🤝 Pembagian Tugas Kelompok
* **Abyan Farisa** (K3525018): Bertanggung jawab atas perancangan logika Binary Search Tree (BST) untuk penyimpanan data menu restoran, penyatuan modul di file `main.py`, dan penyusunan data menu awal (*seeding*).
* **'Azzam Tsabitul Jamil** (K3523001): Bertanggung jawab atas logika struktur data Binary Heap (Max-Heap) prioritas dapur, penentuan aturan bobot prioritas (VIP, makanan, minuman), dan penyusunan integrasi VIP Cashier.
* **Sekar Hanny Keisha Azahra** (K3525041): Bertanggung jawab atas perancangan logika Queue (Antrean Kasir) dan Stack (Riwayat Pesanan), serta perancangan antarmuka visual menu interaktif CLI pada `kasir_view.py`.