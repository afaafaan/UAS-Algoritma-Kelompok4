class StackService:
    def __init__(self):
        self.riwayat = [] # Murni pakai list Python

    def push(self, pesanan):
        self.riwayat.append(pesanan)
        print(f"✅ [RIWAYAT] Pesanan '{pesanan}' selesai dan masuk ke buku riwayat.")

    def pop(self):
        if len(self.riwayat) == 0:
            print("⚠️ [RIWAYAT] Riwayat kosong.")
            return None
        # Mengambil elemen terakhir
        return self.riwayat.pop()

    def display(self):
        if len(self.riwayat) == 0:
            print("[RIWAYAT] Buku Riwayat: KOSONG")
        else:
            # Dibalik (reversed) supaya yang paling baru tampil di atas
            for p in reversed(self.riwayat):
                print(f"  - {p}")
