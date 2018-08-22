fav_items = ["Music", "Technology", "Food"]
fav_size = len(fav_items)
for i in range(fav_size):
    print(str(i+1) + ". " + fav_items[i])

index = int(input("Favorite position you want to get rid of: "))
if index in range(1, fav_size+1):
    fav_items.pop(index-1)
    fav_size = len(fav_items)
    for i in range(fav_size):
        if i < index-1:
            print(i+1, ". ", fav_items[i], sep = "")
        else:
            print(i+2, ". ", fav_items[i], sep = "")
else:
    print("Invalid position. Please try again.")