fav_items = ["Music", "Technology", "Food"]
fav_size = len(fav_items)
for i in range(fav_size):
    print(str(i+1) + ". " + fav_items[i])

item = input("Favorite item you want to get rid of: ")
n = fav_items.index(item)
if item in fav_items:
    fav_items.remove(item)
    fav_size = len(fav_items)
    for i, fav in enumerate(fav_items):
        if i < n:
            print(i+1, ". ", fav_items[i], sep = "")
        else:
            print(i+2, ". ", fav_items[i], sep = "")
else:
    print("Invalid item. Please try again.")