favs = ["Music", "Technology", "Food"]
fav_size = len(favs)
for i, item in enumerate(favs):
    print(i+1, ". ", item, sep = "")

while True:
    command = input("What do you want? (C, R, U, D)? ")
    if command.upper() == "C":
        new_item = input("New item you want to add: ")
        favs.append(new_item)
        print(favs)
    elif command.upper() == "R":
        for i, item in enumerate(favs):
            print(i+1, ". ", item, sep = "")
    elif command.upper() == "U":
        index = int(input("Position you want to update: "))
        update_item = input("Updating item: ")
        favs[index-1] = update_item
        print(favs)
    elif command.upper() == "D":
        choice = input("Do you want to delete by index (I) or item name (N)? ")
        if choice.upper() == "I":
            index = int(input("Position you want to delete: "))
            if index in range(1,fav_size+1):
                favs.pop(index-1)
                fav_size = len(favs)
                for i in range(fav_size):
                    if i < index-1:
                        print(i+1, ". ", favs[i], sep = "")
                    else:
                        print(i+2, ". ", favs[i], sep = "")
            else:
                print("Invalid position")
        elif choice.upper() == "N":
            item = input("Item you want to delete: ")
            n = favs.index(item)
            if item in favs:
                favs.remove(item)
                fav_size = len(favs)
                for i, item in enumerate(favs):
                    if i < n:
                        print(i+1, ". ", favs[i], sep = "")
                    else:
                        print(i+2, ". ", favs[i], sep = "")
            else:
                print("Invalid item")
        else: 
            print("Invalid command")
    else: 
        print("Invalid command")