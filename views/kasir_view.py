class KasirView:
    # Menerima semua service/logika yang dipassing dari main.py nanti
    def __init__(self, queue_svc, stack_svc, bst_svc=None, heap_svc=None):
        self.queue = queue_svc
        self.stack = stack_svc
        self.bst = bst_svc
        self.heap = heap_svc

    def run(self):
        while True:
            print("\n" + "="*40)
            print("🍔 SISTEM MANAJEMEN RESTORAN XYZ 🍔")
            print("="*40)
            print("1. Lihat Daftar Menu Restoran")
            print("2. Kasir: Input Pesanan (Masuk Antrean)")
            print("3. Dapur: Masak Pesanan (Antrean -> Prioritas Dapur)")
            print("4. Koki: Pesanan Selesai (Dapur -> Riwayat)")
            print("5. Lihat Status Antrean & Riwayat")
            print("6. Keluar Aplikasi")
            print("="*40)
            
            pilihan = input("Pilih aksi (1-6): ")

            if pilihan == '1':
                print("\n--- 📖 DAFTAR MENU ---")
                if self.bst:
                    # Nanti memanggil fungsi display dari BST Abyan
                    self.bst.display_menu() 
                else:
                    print("⚠️ Fitur Menu (BST) belum digabungkan oleh Abyan.")
            
            elif pilihan == '2':
                nama_pesanan = input("Masukkan nama pesanan pelanggan: ")
                self.queue.enqueue(nama_pesanan)
            
            elif pilihan == '3':
                pesanan = self.queue.dequeue()
                if pesanan:
                    print(f"--> Membawa '{pesanan}' ke dapur...")
                    if self.heap:
                        # Nanti memanggil fungsi insert dari Heap Kating
                        self.heap.insert(pesanan)
                    else:
                        print("⚠️ Fitur Dapur (Heap) belum digabungkan oleh Kating.")
            
            elif pilihan == '4':
                print("\n--- 🍳 STATUS MASAK ---")
                if self.heap:
                    # Nanti memanggil fungsi hapus/selesai dari Heap Kating
                    pesanan_selesai = self.heap.extract_max() 
                    if pesanan_selesai:
                        self.stack.push(pesanan_selesai)
                else:
                    # Kalau kating belum selesai, kita pakai input manual dulu buat ngetes Stack-nya jalan atau nggak
                    manual = input("Masukkan nama pesanan yang sudah selesai dimasak: ")
                    self.stack.push(manual)
                
            elif pilihan == '5':
                print("\n--- ⏳ ANTREAN KASIR SAAT INI ---")
                self.queue.display()
                print("\n--- 📜 RIWAYAT PESANAN SELESAI ---")
                self.stack.display()
                
            elif pilihan == '6':
                print("Terima kasih! Menutup sistem kasir...")
                break
                
            else:
                print("❌ Pilihan tidak valid, silakan ketik angka 1 sampai 6.")
              
