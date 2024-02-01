path="C:\\Users\\Admin\\Desktop\\mypython\\fileoperations\years.txt"

f=open(path,"w")

for y in range(1800,2025):
    f.write(str(y)+"\n")
