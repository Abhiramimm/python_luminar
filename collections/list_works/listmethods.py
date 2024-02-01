dishes=["vb","cb","bb","gheeroast","friedrice","vb","cb"]

# add dosha to dishes

dishes.append("dosha")
print(dishes)

dishes.insert(1,"nan")
print(dishes)

dishes.pop()
print(dishes)

dishes.pop(4)
print(dishes)

dishes.remove("vb")
print(dishes)

dishes.reverse()
print(dishes)

dishes.sort()
print(dishes)

print(dishes.count("cb"))