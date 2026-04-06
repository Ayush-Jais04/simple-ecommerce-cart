class ProductCatalog:
    def __init__(self):
        # product_id -> (name, price)
        self.products = {
            1: ("T-shirt", 20),
            2: ("Mug", 10),
            3: ("Notebook", 5),
            4: ("Cap", 15)
        }

    def list_products(self):
        print("\nAvailable Products:")
        for pid, (name, price) in self.products.items():
            print(f"  {pid} - {name} - ${price}")
        print()

    def exists(self, product_id):
        return product_id in self.products

    def get(self, product_id):
        return self.products.get(product_id)


class Cart:
    def __init__(self):
        # product_id -> quantity
        self.items = {}

    def add(self, product_id, qty=1):
        if product_id in self.items:
            self.items[product_id] += qty
        else:
            self.items[product_id] = qty

    def remove(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def update(self, product_id, qty):
        if qty <= 0:
            self.remove(product_id)
        else:
            self.items[product_id] = qty

    def clear(self):
        self.items = {}

    def is_empty(self):
        return len(self.items) == 0

    def get_items(self):
        return self.items.copy()


class ShopCLI:
    def __init__(self):
        self.catalog = ProductCatalog()
        self.cart = Cart()

    def show_menu(self):
        print("----- Simple E-commerce (Class Version) -----")
        print("1. Show products")
        print("2. Add to cart")
        print("3. Remove from cart")
        print("4. View cart")
        print("5. Update quantity")
        print("6. Clear cart")
        print("7. Checkout")
        print("8. Exit")
        print("--------------------------------------------")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter choice (1-8): ").strip()
            if choice == "1":
                self.catalog.list_products()
            elif choice == "2":
                self.handle_add()
            elif choice == "3":
                self.handle_remove()
            elif choice == "4":
                self.handle_view()
            elif choice == "5":
                self.handle_update()
            elif choice == "6":
                self.handle_clear()
            elif choice == "7":
                self.handle_checkout()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.\n")

    def handle_add(self):
        try:
            pid = int(input("Enter product ID to add: ").strip())
        except ValueError:
            print("Invalid input. Use a number.\n")
            return
        if not self.catalog.exists(pid):
            print("Product ID does not exist.\n")
            return
        self.cart.add(pid, 1)
        name, _ = self.catalog.get(pid)
        print(f"Added 1 x {name} to cart.\n")

    def handle_remove(self):
        try:
            pid = int(input("Enter product ID to remove from cart: ").strip())
        except ValueError:
            print("Invalid input. Use a number.\n")
            return
        if pid not in self.cart.get_items():
            print("That item is not in your cart.\n")
            return
        self.cart.remove(pid)
        print("Item removed from cart.\n")

    def handle_view(self):
        if self.cart.is_empty():
            print("\nYour cart is empty.\n")
            return
        print("\nYour cart:")
        total = 0
        for pid, qty in self.cart.get_items().items():
            name, price = self.catalog.get(pid)
            line = price * qty
            total += line
            print(f"  {name} - Qty: {qty} - Line total: ${line}")
        print(f"Total amount: ${total}\n")

    def handle_update(self):
        try:
            pid = int(input("Enter product ID to update: ").strip())
        except ValueError:
            print("Invalid input. Use a number.\n")
            return
        if pid not in self.cart.get_items():
            print("That item is not in your cart.\n")
            return
        try:
            qty = int(input("Enter new quantity (0 to remove): ").strip())
        except ValueError:
            print("Invalid input. Use a number.\n")
            return
        self.cart.update(pid, qty)
        print("Quantity updated.\n")

    def handle_clear(self):
        self.cart.clear()
        print("Cart cleared.\n")

    def handle_checkout(self):
        if self.cart.is_empty():
            print("Cart is empty. Nothing to checkout.\n")
            return
        self.handle_view()
        confirm = input("Proceed to checkout? (y/n): ").strip().lower()
        if confirm == "y":
            print("Checkout complete. Thank you for your purchase!\n")
            self.cart.clear()
        else:
            print("Checkout cancelled.\n")


if __name__ == "__main__":
    shop = ShopCLI()
    shop.run()
