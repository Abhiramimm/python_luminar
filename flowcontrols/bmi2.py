weight_in_kg=int(input("Enter weight:"))

height_in_cm=int(input("Enter height:"))

height_in_m=height_in_cm/100

bmi=weight_in_kg//(height_in_m)**2

print(bmi)

if bmi<18:
    print("uderweight")
elif bmi <25:
    print("healthy")
elif bmi <30:
    print("over weight")
elif bmi <35:
    print("obese")
elif bmi>=35:
    print("severe obesity")