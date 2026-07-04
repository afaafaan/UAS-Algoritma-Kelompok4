from services.bst_service import BSTMenu
from services.queue_service import QueueAntrean
from services.heap_service import HeapPrioritas
from services.stack_service import StackRiwayat
from views.kasir_view import tampilkan_menu_utama


def seed_menu_awal(bst: BSTMenu):
    data_awal = [
        ("M001", "Nasi Goreng", 20000, "Makanan"),
        ("M002", "Es Teh", 5000, "Minuman"),
        ("M003", "Ayam Bakar", 25000, "Makanan"),
        ("M004", "Puding Coklat", 12000, "Dessert"),
        ("M005", "Mie Goreng", 18000, "Makanan"),
    ]
    for id_menu, nama, harga, kategori in data_awal:
        bst.insert(id_menu, nama, harga, kategori)


def menu_tambah_pesanan(queue: QueueAntrean):
    nama_pelanggan = input("Nama pelanggan: ").strip()
    nama_menu = input("Nama menu yang dipesan: ").strip()
    is_vip = input("Apakah pesanan mendesak/VIP? (y/n): ").strip().lower() == "y"

    pesanan = {
        "pelanggan": nama_pelanggan,
        "menu": nama_menu,
        "prioritas": 1 if is_vip else 2,
    }
    queue.enqueue(pesanan)
    print(f"Pesanan '{nama_menu}' atas nama {nama_pelanggan} berhasil masuk antrean.")


def menu_proses_antrean(queue: QueueAntrean, bst: BSTMenu, heap: HeapPrioritas):
    if queue.is_empty():
        print("Antrean pesanan kosong, tidak ada yang diproses.")
        return

    pesanan = queue.dequeue()
    hasil_cari = bst.search(pesanan["menu"])

    if hasil_cari is None:
        print(f"Menu '{pesanan['menu']}' tidak ditemukan di daftar menu. Pesanan dibatalkan.")
        return

    pesanan["harga"] = hasil_cari.harga
    pesanan["id_menu"] = hasil_cari.id_menu

    heap.insert(pesanan["prioritas"], pesanan)
    print(f"Pesanan {pesanan['pelanggan']} ({pesanan['menu']}, Rp{hasil_cari.harga}) "
          f"masuk antrean dapur dengan prioritas {pesanan['prioritas']}.")


def menu_proses_dapur(heap: HeapPrioritas, stack: StackRiwayat):
    if heap.is_empty():
        print("Tidak ada pesanan yang menunggu diproses dapur.")
        return

    prioritas, pesanan = heap.delete_root()
    print(f"Dapur memproses pesanan {pesanan['pelanggan']} - {pesanan['menu']} "
          f"(prioritas {prioritas})...")

    stack.push(pesanan)
    print("Pesanan selesai dan dicatat ke riwayat.")


def menu_lihat_riwayat(stack: StackRiwayat):
    stack.display()


def menu_undo_pesanan(stack: StackRiwayat):
    dibatalkan = stack.pop()
    if dibatalkan is None:
        print("Tidak ada riwayat pesanan untuk dibatalkan.")
    else:
        print(f"Pesanan terakhir dibatalkan: {dibatalkan['pelanggan']} - {dibatalkan['menu']}")


def menu_kelola_menu(bst: BSTMenu):
    print("\n1. Tambah menu")
    print("2. Cari menu")
    print("3. Hapus menu")
    print("4. Tampilkan semua menu")
    pilihan = input("Pilih aksi: ").strip()

    if pilihan == "1":
        id_menu = input("ID menu: ").strip()
        nama = input("Nama menu: ").strip()
        harga = int(input("Harga: ").strip())
        kategori = input("Kategori: ").strip()
        bst.insert(id_menu, nama, harga, kategori)
        print("Menu berhasil ditambahkan.")
    elif pilihan == "2":
        nama = input("Nama menu yang dicari: ").strip()
        hasil = bst.search(nama)
        print("Ditemukan:", hasil if hasil else "Menu tidak ada.")
    elif pilihan == "3":
        nama = input("Nama menu yang dihapus: ").strip()
        berhasil = bst.delete(nama)
        print("Berhasil dihapus." if berhasil else "Menu tidak ditemukan.")
    elif pilihan == "4":
        bst.display()
    else:
        print("Pilihan tidak valid.")


def menu_info_tree(bst: BSTMenu):
    print(f"Tinggi tree menu: {bst.get_height()}")
    print(f"Jumlah node (jumlah menu): {bst.count_nodes()}")


def main():
    bst_menu = BSTMenu()
    queue_pesanan = QueueAntrean()
    heap_dapur = HeapPrioritas()
    stack_riwayat = StackRiwayat()

    seed_menu_awal(bst_menu)

    while True:
        pilihan = tampilkan_menu_utama()

        if pilihan == "1":
            menu_tambah_pesanan(queue_pesanan)
        elif pilihan == "2":
            menu_proses_antrean(queue_pesanan, bst_menu, heap_dapur)
        elif pilihan == "3":
            menu_proses_dapur(heap_dapur, stack_riwayat)
        elif pilihan == "4":
            menu_lihat_riwayat(stack_riwayat)
        elif pilihan == "5":
            menu_undo_pesanan(stack_riwayat)
        elif pilihan == "6":
            menu_kelola_menu(bst_menu)
        elif pilihan == "7":
            menu_info_tree(bst_menu)
        elif pilihan == "0":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")


if __name__ == "__main__":
    main()