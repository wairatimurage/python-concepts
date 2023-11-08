height = 2.1
weight = 150
bmi = weight / height ** 2

print(f"BMI is {bmi}")

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Healthy")
elif 25 <= bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")
