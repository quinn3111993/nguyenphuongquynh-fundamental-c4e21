import getpass

user_name = "c4e"
password = "codethechange"

print("Hi there, this is a superuser gateway")
name_input = input("Username: ")
if name_input == user_name:
    pass_input = getpass.getpass("Password: ")
    if pass_input == password:
        print("Welcome, c4e")
    else:
        print("Password is incorrect")
else:
    print("You are not superuser")

