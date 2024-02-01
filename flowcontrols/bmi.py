weight_in_kg=int(input("Enter weight:"))

height_in_cm=int(input("Enter height:"))

height_in_m=height_in_cm/100

bmi=weight_in_kg//(height_in_m)**2

print(bmi)

if bmi<18:
    print("You are uderweight")
elif bmi>=18 and bmi <25:
    print("You are healthy")
elif bmi>=25 and bmi <30:
    print("You are over weight")
elif bmi>=30 and bmi <35:
    print("obese")
elif bmi>35:
    print("severe obesity")