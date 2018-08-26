my_dic = {
    "fyi": "for your information", 
    "anw": "anyways", 
    "tks": "thanks", 
    "dtb": "database",
    }
while True:
    user_key = input("Your key: ")
    if user_key in my_dic:
        print(user_key, ": ", my_dic[user_key], sep="")
    else:
        q = input("Invalid key. Do you want to add? (Y/N) ").upper()
        if q == "Y":
            user_input = input("Your definition: ")
            my_dic[user_key] = user_input
            print("Added successfully!")
        elif q == "N":
            print("Thanks!")
        else:
            print("invalid answer!")
