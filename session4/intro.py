# person = ["Quan", 20, "Hanoi", "Thang Long", 3, "Da Nang"]
# print(person)

# person = {

# }

# print(person)

# person = {
#     "name": "Quan"
# }

# print(person)

person = {
    "name": "Quan",
    "age": 20,
    "city": "hanoi",
}

# del person["age"]
# print(person)

for k in person.keys():
    print(k)

for v in person.values():
    print(v)

for k, v in person.items():
    print(k, ":", v)

# print(person["status"])
# person["status"] = "complicated"
# print(person)

# print(person)
# print(person["city"])
# person["city"] = "danang"
# print(person)

# key = "city"
# print(person[key])