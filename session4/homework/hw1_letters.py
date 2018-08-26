import collections

input_string = input("Enter your string: ").lower()
char_list = list(input_string)
letter_count = {}

for char in char_list:
    if char != " ":
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1

ordered_letter = collections.OrderedDict(sorted(letter_count.items()))

for k, v in ordered_letter.items():
    print(k, v)
        

