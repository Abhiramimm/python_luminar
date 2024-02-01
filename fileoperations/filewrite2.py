lst=["red","green","blue","white","black","yellow"]
path="C:\\Users\\Admin\\Desktop\\mypython\\fileoperations\\colors.txt"

fw=open(path,"w")
for c in lst:
    fw.write(c+"\n")