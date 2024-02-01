path="C:\\Users\\Admin\\Desktop\\mypython\\fileoperations\\colors.txt"

f=open(path,"r")

colors_list=[]

for line in f:
    colors_list.append(line.rstrip("\n"))
print(colors_list)
    
print(set(colors_list)) #remove duplicates from colors.txt