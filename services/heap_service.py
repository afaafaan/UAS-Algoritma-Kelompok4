class HeapPrioritas:
    """
    Max-Heap untuk antrean prioritas dapur restoran.
    Elemen dengan prioritas lebih tinggi selalu berada di root.
    Implementasi berbasis array (list Python), tanpa library heap bawaan.
    """

    def __init__(self):
        self.data = []
        self._counter = 0

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def _lebih_prioritas(self, index_a, index_b):
        """True jika elemen index_a lebih prioritas daripada index_b."""
        a = self.data[index_a]
        b = self.data[index_b]
        if a["prioritas"] != b["prioritas"]:
            return a["prioritas"] > b["prioritas"]
        return a["urutan"] < b["urutan"]

    def _tentukan_prioritas(self, nama_pesanan, kategori=None):
        """Tentukan skala prioritas berdasarkan jenis pesanan."""
        nama = nama_pesanan.lower()
        if "vip" in nama:
            return 5
        if kategori:
            kat = kategori.lower()
            if kat in ("minuman", "dessert"):
                return 3
            if kat == "makanan":
                return 2
        if any(kata in nama for kata in ["es ", "teh", "minuman", "puding", "dessert"]):
            return 3
        if any(kata in nama for kata in ["nasi", "ayam", "mie", "goreng", "bakar"]):
            return 2
        return 1

    # ------------------------------------------------------------------
    # HEAPIFY UP -> O(log n)
    # ------------------------------------------------------------------
    def heapify_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self._lebih_prioritas(index, parent):
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    # ------------------------------------------------------------------
    # HEAPIFY DOWN -> O(log n)
    # ------------------------------------------------------------------
    def heapify_down(self, index):
        n = len(self.data)
        while True:
            largest = index
            left = self._left(index)
            right = self._right(index)

            if left < n and self._lebih_prioritas(left, largest):
                largest = left
            if right < n and self._lebih_prioritas(right, largest):
                largest = right

            if largest != index:
                self.data[index], self.data[largest] = self.data[largest], self.data[index]
                index = largest
            else:
                break

    # ------------------------------------------------------------------
    # INSERT -> O(log n)
    # ------------------------------------------------------------------
    def insert(self, nama_pesanan, prioritas=None, kategori=None):
        if prioritas is None:
            prioritas = self._tentukan_prioritas(nama_pesanan, kategori)

        self._counter += 1
        self.data.append({
            "nama": nama_pesanan,
            "prioritas": prioritas,
            "urutan": self._counter,
        })
        self.heapify_up(len(self.data) - 1)
        print(
            f"✅ [DAPUR] Pesanan '{nama_pesanan}' masuk antrean dapur "
            f"(prioritas: {prioritas})."
        )

    # ------------------------------------------------------------------
    # PEEK -> O(1)
    # ------------------------------------------------------------------
    def peek(self):
        if not self.data:
            return None
        return self.data[0]["nama"]

    def peek_detail(self):
        if not self.data:
            return None
        return self.data[0].copy()

    # ------------------------------------------------------------------
    # DELETE ROOT -> O(log n)
    # ------------------------------------------------------------------
    def delete_root(self):
        if not self.data:
            return None

        root = self.data[0]
        last = self.data.pop()

        if self.data:
            self.data[0] = last
            self.heapify_down(0)

        return root

    def extract_max(self):
        """Ambil pesanan prioritas tertinggi dari dapur (alias delete root)."""
        item = self.delete_root()
        if item is None:
            print("⚠️ [DAPUR] Tidak ada pesanan di dapur.")
            return None

        print(
            f"🍳 [DAPUR] Pesanan '{item['nama']}' selesai dimasak "
            f"(prioritas: {item['prioritas']})."
        )
        return item["nama"]

    # ------------------------------------------------------------------
    # DISPLAY -> O(n log n) untuk urutan tampilan
    # ------------------------------------------------------------------
    def display(self):
        if not self.data:
            print("[DAPUR] Antrean Prioritas: KOSONG")
            return

        print("[DAPUR] Antrean Prioritas Dapur:")
        urutan_tampil = sorted(
            self.data,
            key=lambda x: (-x["prioritas"], x["urutan"]),
        )
        for i, item in enumerate(urutan_tampil, start=1):
            tanda = " ⭐ ROOT" if item is self.data[0] else ""
            print(
                f"  {i}. {item['nama']:<20} | Prioritas: {item['prioritas']}{tanda}"
            )

        root = self.peek_detail()
        if root:
            print(f"  → Berikutnya dimasak: {root['nama']} (prioritas {root['prioritas']})")


if __name__ == "__main__":
    heap = HeapPrioritas()

    heap.insert("Nasi Goreng")
    heap.insert("Es Teh")
    heap.insert("VIP Ayam Bakar")

    print("\nPeek:", heap.peek())
    heap.display()

    print("\nExtract max:", heap.extract_max())
    print("Extract max:", heap.extract_max())
    print("Extract max:", heap.extract_max())
    print("Extract max:", heap.extract_max())
