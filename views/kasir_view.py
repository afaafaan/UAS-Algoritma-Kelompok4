class KasirView:
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
                    self.bst.display_menu()
                else:
                    print("⚠️ Fitur Menu (BST) belum digabungkan.")

            elif pilihan == '2':
                nama_pesanan = input("Masukkan nama pesanan (lihat menu di opsi 1): ").strip()
                if not nama_pesanan:
                    print("❌ Nama pesanan tidak boleh kosong.")
                    continue

                if self.bst:
                    menu = self.bst.search(nama_pesanan)
                    if menu is None:
                        print(f"❌ Menu '{nama_pesanan}' tidak ditemukan. Cek daftar menu (opsi 1).")
                        continue
                    is_vip_input = input("Apakah pelanggan VIP? (y/n): ").strip().lower()
                    is_vip = is_vip_input == 'y'
                    self.queue.enqueue(menu.nama_menu, is_vip=is_vip)
                else:
                    is_vip_input = input("Apakah pelanggan VIP? (y/n): ").strip().lower()
                    is_vip = is_vip_input == 'y'
                    self.queue.enqueue(nama_pesanan, is_vip=is_vip)

            elif pilihan == '3':
                pesanan_dict = self.queue.dequeue()
                if pesanan_dict:
                    pesanan_nama = pesanan_dict["display_name"]
                    nama_asli = pesanan_dict["nama_asli"]
                    print(f"--> Membawa '{pesanan_nama}' ke dapur...")
                    if self.heap:
                        kategori = None
                        if self.bst:
                            menu = self.bst.search(nama_asli)
                            if menu:
                                kategori = menu.kategori
                        self.heap.insert(pesanan_nama, kategori=kategori)
                    else:
                        print("⚠️ Fitur Dapur (Heap) belum digabungkan.")

            elif pilihan == '4':
                print("\n--- 🍳 STATUS MASAK ---")
                if self.heap:
                    pesanan_selesai = self.heap.extract_max()
                    if pesanan_selesai:
                        self.stack.push(pesanan_selesai)
                else:
                    manual = input("Masukkan nama pesanan yang sudah selesai dimasak: ")
                    self.stack.push(manual)

            elif pilihan == '5':
                print("\n--- ⏳ ANTREAN KASIR SAAT INI ---")
                self.queue.display()
                antrean_depan = self.queue.peek()
                if antrean_depan:
                    if isinstance(antrean_depan, dict):
                        print(f"  → Peek antrean: {antrean_depan['display_name']}")
                    else:
                        print(f"  → Peek antrean: {antrean_depan}")

                print("\n--- 🍳 ANTREAN DAPUR (HEAP) ---")
                if self.heap:
                    self.heap.display()
                else:
                    print("⚠️ Fitur Dapur (Heap) belum digabungkan.")

                print("\n--- 📜 RIWAYAT PESANAN SELESAI ---")
                self.stack.display()
                riwayat_teratas = self.stack.peek()
                if riwayat_teratas:
                    print(f"  → Peek riwayat terakhir: {riwayat_teratas}")

            elif pilihan == '6':
                print("Terima kasih! Menutup sistem kasir...")
                break

            else:
                print("❌ Pilihan tidak valid, silakan ketik angka 1 sampai 6.")
