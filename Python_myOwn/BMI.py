weight = input("ENTER the WEIGHT in KGs:")
height = input("ENTER the HEIGHT in Meters:")
print(f"Entered weight is {weight} and height is {height}")

BMI = round(float(weight) / (float(height) ** 2), 2)

if BMI <= 18.5:
    print(f"Your BMI is {BMI}. You are UNDERWEIGHT.")
elif BMI < 25:
    print(f"Your BMI is {BMI}. You are NORMAL.")
elif BMI < 30:
    print(f"Your BMI is {BMI}. You are OVERWEIGHT.")
else:
    print(f"Your BMI is {BMI}. You are OBESE.")
