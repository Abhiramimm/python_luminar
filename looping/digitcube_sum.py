# num=2
# cube=2**3
# print(cube)
# ---------------
num=345
sum=0
while(num!=0):
    digit=num%10
    cube=digit**3
    sum=sum+cube
    num=num//10
    #print(cube)
    print(f"sum of cubes  = {sum}")
