from models.node_menu import NodeMenu


class BSTMenu:
    def __init__(self):
        self.root = None

    # ------------------------------------------------------------------
    # INSERT -> O(log n) rata-rata, O(n) worst case (tree tidak seimbang)
    # ------------------------------------------------------------------
    def insert(self, id_menu, nama_menu, harga, kategori):
        node_baru = NodeMenu(id_menu, nama_menu, harga, kategori)
        if self.root is None:
            self.root = node_baru
        else:
            self._insert_rec(self.root, node_baru)

    def _insert_rec(self, current, node_baru):
        key_current = current.nama_menu.lower()
        key_baru = node_baru.nama_menu.lower()

        if key_baru < key_current:
            if current.left is None:
                current.left = node_baru
            else:
                self._insert_rec(current.left, node_baru)
        elif key_baru > key_current:
            if current.right is None:
                current.right = node_baru
            else:
                self._insert_rec(current.right, node_baru)
        else:
            # Nama menu sama persis -> anggap update harga & kategori
            current.harga = node_baru.harga
            current.kategori = node_baru.kategori
            current.id_menu = node_baru.id_menu

    # ------------------------------------------------------------------
    # SEARCH -> O(log n) rata-rata, O(n) worst case
    # ------------------------------------------------------------------
    def search(self, nama_menu):
        return self._search_rec(self.root, nama_menu.lower())

    def _search_rec(self, current, key):
        if current is None:
            return None
        key_current = current.nama_menu.lower()
        if key == key_current:
            return current
        elif key < key_current:
            return self._search_rec(current.left, key)
        else:
            return self._search_rec(current.right, key)

    # ------------------------------------------------------------------
    # DELETE -> O(log n) rata-rata, O(n) worst case
    # 3 kasus: node tanpa anak, node dengan 1 anak, node dengan 2 anak
    # ------------------------------------------------------------------
    def delete(self, nama_menu):
        self.root, berhasil = self._delete_rec(self.root, nama_menu.lower())
        return berhasil

    def _delete_rec(self, current, key):
        if current is None:
            return current, False

        key_current = current.nama_menu.lower()

        if key < key_current:
            current.left, berhasil = self._delete_rec(current.left, key)
            return current, berhasil
        elif key > key_current:
            current.right, berhasil = self._delete_rec(current.right, key)
            return current, berhasil
        else:
            # Node ditemukan, ini yang mau dihapus
            # Kasus 1: tidak punya anak sama sekali
            if current.left is None and current.right is None:
                return None, True
            # Kasus 2: hanya punya satu anak
            if current.left is None:
                return current.right, True
            if current.right is None:
                return current.left, True
            # Kasus 3: punya dua anak
            # Cari inorder successor (node terkecil di subtree kanan)
            successor = self._cari_min(current.right)
            current.id_menu = successor.id_menu
            current.nama_menu = successor.nama_menu
            current.harga = successor.harga
            current.kategori = successor.kategori
            current.right, _ = self._delete_rec(current.right, successor.nama_menu.lower())
            return current, True

    def _cari_min(self, current):
        while current.left is not None:
            current = current.left
        return current

    # ------------------------------------------------------------------
    # TRAVERSAL INORDER -> O(n), mengunjungi seluruh node
    # ------------------------------------------------------------------
    def inorder(self):
        hasil = []
        self._inorder_rec(self.root, hasil)
        return hasil

    def _inorder_rec(self, current, hasil):
        if current is not None:
            self._inorder_rec(current.left, hasil)
            hasil.append(current)
            self._inorder_rec(current.right, hasil)

    # ------------------------------------------------------------------
    # HEIGHT -> O(n), harus cek semua node untuk cari kedalaman maksimum
    # ------------------------------------------------------------------
    def get_height(self):
        return self._height_rec(self.root)

    def _height_rec(self, current):
        if current is None:
            return -1  # tree kosong = -1, node tunggal = 0
        kiri = self._height_rec(current.left)
        kanan = self._height_rec(current.right)
        return 1 + max(kiri, kanan)

    # ------------------------------------------------------------------
    # COUNT NODES -> O(n)
    # ------------------------------------------------------------------
    def count_nodes(self):
        return self._count_rec(self.root)

    def _count_rec(self, current):
        if current is None:
            return 0
        return 1 + self._count_rec(current.left) + self._count_rec(current.right)

    def display_menu(self):
        daftar = self.inorder()
        if not daftar:
            print("Menu masih kosong.")
            return
        print("=== DAFTAR MENU (Alfabetis) ===")
        for node in daftar:
            print(f"{node.id_menu} | {node.nama_menu:<20} | Rp{node.harga:<10} | {node.kategori}")

if __name__ == "__main__":
    bst = BSTMenu()
    bst.insert("M001", "Nasi Goreng", 20000, "Makanan")
    bst.insert("M002", "Es Teh", 5000, "Minuman")
    bst.insert("M003", "Ayam Bakar", 25000, "Makanan")
    bst.insert("M004", "Puding Coklat", 12000, "Dessert")

    bst.display_menu()
    print("\nTinggi tree:", bst.get_height())
    print("Jumlah node:", bst.count_nodes())

    hasil_cari = bst.search("Es Teh")
    print("\nHasil search 'Es Teh':", hasil_cari)

    bst.delete("Nasi Goreng")
    print("\nSetelah hapus 'Nasi Goreng':")
    bst.display_menu()
