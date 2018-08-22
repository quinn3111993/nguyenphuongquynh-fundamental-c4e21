fav_items = ["Music", "Technology", "Food"]
fav_size = len(fav_items)
for i in range(fav_size):
    print(str(i+1) + ". " + fav_items[i])

index = int(input("Position you want to update: "))
if index in range(1, fav_size+1):
    item = input("Your replacing item: ")
    fav_items[index-1] = item
    for i in range(fav_size):
        print(str(i+1) + ". " + fav_items[i])
else:
    print("Invalid position. Please try again.")


