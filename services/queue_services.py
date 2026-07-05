class QueueService:
    def __init__(self):
        self.antrean = [] # Murni pakai list Python

    def enqueue(self, pesanan):
        self.antrean.append(pesanan)
        print(f"✅ [KASIR] Pesanan '{pesanan}' berhasil masuk ke antrean.")

    def dequeue(self):
        if len(self.antrean) == 0:
            print("⚠️ [KASIR] Antrean kosong, belum ada pesanan.")
            return None
        # Mengambil indeks ke-0 (paling depan)
        return self.antrean.pop(0)

    def peek(self):
        if len(self.antrean) == 0:
            return None
        return self.antrean[0]

    def display(self):
        if len(self.antrean) == 0:
            print("[KASIR] Status Antrean: KOSONG")
        else:
            for i, p in enumerate(self.antrean):
                print(f"  {i + 1}. {p}")
              
