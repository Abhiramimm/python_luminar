num1=4
num2=24
hcf=1
i=1

while(i<=num1 or i<=num2):
  if (num1%i==0) and (num2%i==0):
    hcf=i
  i=i+1
print(f"hcf of {num1} and {num2} = {hcf}")
