class NodeMenu:
    """Node untuk Binary Search Tree menu restoran."""

    def __init__(self, id_menu, nama_menu, harga, kategori):
        self.id_menu = id_menu
        self.nama_menu = nama_menu
        self.harga = harga
        self.kategori = kategori
        self.left = None
        self.right = None

    def __repr__(self):
        return f"NodeMenu({self.id_menu}, {self.nama_menu}, {self.harga}, {self.kategori})"
