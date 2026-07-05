from services.bst_services import BSTMenu
from services.queue_services import QueueService
from services.stack_services import StackService
from services.heap_service import HeapPrioritas
from views.kasir_view import KasirView


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


def main():
    bst_menu = BSTMenu()
    queue_svc = QueueService()
    stack_svc = StackService()
    heap_svc = HeapPrioritas()

    seed_menu_awal(bst_menu)

    kasir = KasirView(
        queue_svc=queue_svc,
        stack_svc=stack_svc,
        bst_svc=bst_menu,
        heap_svc=heap_svc,
    )
    kasir.run()


if __name__ == "__main__":
    main()
