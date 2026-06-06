#Smart Inventory Management System
inventory = {}

while True:
    print("\n1.Add Product")
    print("2.View Products")
    print("3.Search Product")
    print("4.Delete Product")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Product Name: ")
        qty = int(input("Quantity: "))
        inventory[name] = qty
        print("Product Added")

    elif choice == "2":
        print("\nInventory:")
        for name, qty in inventory.items():
            print(name, "-", qty)

    elif choice == "3":
        name = input("Enter Product Name: ")
        if name in inventory:
            print("Quantity:", inventory[name])
        else:
            print("Product Not Found")

    elif choice == "4":
        name = input("Enter Product Name: ")
        if name in inventory:
            del inventory[name]
            print("Product Deleted")
        else:
            print("Product Not Found")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")f