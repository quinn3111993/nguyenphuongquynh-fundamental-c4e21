import pyexcel
from collections import OrderedDict

r1 = {
    "ten": "Huy",
    "luong": 25,
    "so gio lam": 14,
}
r2 = {
    "ten": "Hoa",
    "luong": 20,
    "so gio lam": 7,
}
r3 = {
    "ten": "Tam",
    "luong": 15,
    "so gio lam": 20,
}
my_list = [r1, r2, r3]
print(my_list)

wage_list = []
tong_cong = 0
for salary in my_list:
    name = salary["ten"]
    hour = salary["so gio lam"]
    level = salary["luong"]
    wage_info = OrderedDict({
        "name": name,
        "wage": hour*level
    })
    wage_list.append(wage_info)
    wage = salary["luong"]*salary["so gio lam"]
    tong_cong += wage
    print("Tien cong cua", salary["ten"], "la", wage)
print("Tong tien cong phai tra:", tong_cong)
print(wage_list)
pyexcel.save_as(records=wage_list, dest_file_name="sample2.xlsx")
