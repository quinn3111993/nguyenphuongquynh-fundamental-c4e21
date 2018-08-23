from random import shuffle

word = "champion"
chars = list(word)
len_chars = len(chars)

shuffle(chars)
for i in range(len_chars):
    print(chars[i], end=" ")
print()
answer = input("Your answer: ")
if answer == word:
    print("hura")
else:
    print(":(")
