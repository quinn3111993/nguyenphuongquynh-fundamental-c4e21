# Write a program that converts Celsius (0C) into Fahrenheit (0F) 

print("Hi, we're converting Celsius to Fahrenheit!")
c_input = int(input("Enter temperature in Celsius: "))
f_output = c_input*1.8 + 32
print(c_input, "(C) =", f_output, "(F)")