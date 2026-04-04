import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    """Parse command-line arguments into an inventory dictionary."""
    inventory: dict[str, int] = {}
    for param in args:
        parts = param.split(":")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error - invalid parameter '{param}'")
            continue
        item_name, quantity_str = parts[0], parts[1]
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            quantity = int(quantity_str)
            inventory[item_name] = quantity
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
    return inventory


def display_inventory_stats(inventory: dict[str, int]) -> None:
    """Display inventory statistics."""
    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    for item, qty in inventory.items():
        percentage = round(qty / total * 100, 1)
        print(f"Item {item} represents {percentage}%")

    keys = list(inventory.keys())
    most = max(keys, key=lambda k: (inventory[k], -keys.index(k)))
    least = min(keys, key=lambda k: (inventory[k], keys.index(k)))

    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")


def main() -> None:
    """Main function to run the inventory system."""
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])

    if not inventory:
        print("No valid items provided.")
        return

    display_inventory_stats(inventory)

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
