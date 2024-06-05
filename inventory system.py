#inventory sysytem
def add_item(inventory):
    item = input("Enter the item name: ")
    quantity = int(input(f"Enter the quantity for {item}: "))
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def retrieve_item(inventory):
    item = input("Enter the item name to retrieve: ")
    if item in inventory:
        print(f"{item}: {inventory[item]}")
    else:
        print(f"{item} is not in the inventory.")

def total_quantity(inventory):
    total = sum(inventory.values())
    print(f"Total quantity of all items: {total}")

def main():
    inventory = {}
    while True:
        print("\n1. Add item")
        print("2. Retrieve item information")
        print("3. Display total quantity of all items")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            retrieve_item(inventory)
        elif choice == '3':
            total_quantity(inventory)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
