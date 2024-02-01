i=1
while(i<=100):
   if (i%15==0):           #i%3 and i%5=i%15
      print("abcdef")
   elif(i%3==0):
      print("abc")
   elif(i%5==0):
      print("def")
   else:
      print(i)
   i+=1