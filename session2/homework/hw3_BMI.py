#Write a program that asks user their height (cm) and weight (kg), and then calculate their BMI 
h = int(input("Your height (cm): "))
w = int(input("Your weight (kg): "))

h_m = h/100
bmi_index = w/(h_m**2)

if bmi_index < 16:
    print("Severely underweigh!")
elif bmi_index < 18.5:
    print("Underweight!")
elif bmi_index < 25:
    print("Normal!")
elif bmi_index < 30:
    print("Overweight!")
else:
    print("Obese!")
