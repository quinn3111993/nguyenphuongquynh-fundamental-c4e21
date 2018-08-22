items = ["T-Shirt", "Sweater"]

while True:
    command = input("Welcome to our shop, what do you want (C, R, U, D)? ").upper()
    if command == "C":
        new_item = input("Enter new item: ")
        items.append(new_item)
        print("Our items:", end=" ") 
        print(*items, sep=", ")
    elif command == "R":
        print("Our items:", end=" ") 
        print(*items, sep=", ")
    elif command == "U":
        index = int(input("Update position? "))
        if index in range(1, len(items)+1):
            new_item = input("New item? ")
            items[index-1] = new_item
            print("Our items:", end=" ") 
            print(*items, sep=", ")
        else: 
            print("Invalid index!")
    elif command == "D":
        index = int(input("Delete position? "))
        if index in range(1, len(items)+1):
            items.pop(index-1)
            print("Our items:", end=" ") 
            print(*items, sep=", ")
        else:
            print("Invalid index!")
    else:
        print("Invalid command!")
