class StoreInventory:
    def __init__(self):
        self.store_inv = {}

    def add_item(self, p_name, name, category, quantity):
        if category not in self.store_inv:
            self.store_inv[category] = {}

        if p_name not in self.store_inv[category]:
            self.store_inv[category][p_name] = {}  # Initialize p_name if it doesn't exist

        if name in self.store_inv[category][p_name]:
            self.store_inv[category][p_name][name] += quantity  # Add to existing quantity
        else:
            self.store_inv[category][p_name][name] = quantity  # Set new quantity

    def display_inventory(self):
        # Check if the store inventory is empty
        if not self.store_inv:
            print("No items in inventory.")
            return

        # Loop through each category in the inventory
        for category, products in self.store_inv.items():
            print(f"Category: {category}")

            # Loop through each product in the category
            for p_name, items in products.items():
                print(f"  Product: {p_name}")

                # Loop through each item in the product
                for name, quantity in items.items():
                    print(f"    Item: {name}, Quantity: {quantity}")

            print("\n" + "-" * 40)  # Add a separator for clarity


def main():
    store = StoreInventory()

    store.add_item ("Amjad", "Chairs", "Furniture", 5)
    store.add_item("Umar", "PC", "Electronics", 2)
    store.add_item("Amjad","Curtain", "Decoration", 3)
    store.add_item("Umar", "Pencils", "Stationary", 5)

    store.display_inventory()

if __name__ == "__main__":
    main()
