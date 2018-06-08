mass = int(input("What's your weight?"))
height_cm = int(input("What's your height?"))
height_m = float(height_cm/100)
BMI = mass / (height_m**2)
if BMI < 16:
    print("Severely underweight")
elif 16 < BMI < 18.5:
    print("Underweight")
elif 18.5<BMI<25:
    print("Normal")
elif 25<BMI<30:
    print("Overweight")
else:
    print("Obese")
