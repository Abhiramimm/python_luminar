product={"code":1000,"name":"hp","category":"laptop","price":50000}
print(product["name"])

#color:black
product["color"]="black"
print(product)

#update product price as 30000
product["price"]=30000
print(product)

# check offer key is present or not
print("offer" in product)

#add offer as 300 if key is not present else update offer as 250
if "offer" in product:
    product["offer"]=250
else:
    product["offer"]=300
print(product)