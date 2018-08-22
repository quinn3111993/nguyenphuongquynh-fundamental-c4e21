fav_items = ["Music", "Technology"]
new_fav = input("Suggest 1 of your fafourite things: ")
fav_items.insert(0, new_fav)
print(*fav_items, sep = ", ")

fav_size = len(fav_items)
#fori
for i in range(fav_size):
    print(str(i+1) + ". " + fav_items[i])