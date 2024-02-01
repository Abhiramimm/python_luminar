name="hello python"
print(name.capitalize())

name2="HELLO PYTHON"
print(name2.casefold())

name3="123"
print(name3.isdigit())

name4="hellopython"
print(name4.isalpha())

name5="hello123"
print(name5.isalnum())

name6="hellopythonpy"
print(name6.index("py"))
print(name6.startswith("he"))
print(name6.endswith("lo"))

name7="hello python welcome"
words=name7.split(" ")
print(words)

name8="hello,python,welcome"
words1=name8.split(",")
print(words1)

name9="hello,python,welcome"
print(name9.count("o"))

name10="#hello#"
# print(name10.strip("#"))
# print(name10.lstrip("#"))
print(name10.rstrip("#"))


sequence=(10,2,3,4,50)
total=sum(sequence)
print(total)

max_num=max(sequence)
print(max_num)

min_num=min(sequence)
print(min_num)

srt=sorted(sequence)
print(srt)

srt1=sorted(sequence,reverse=True)
print(srt1)

text="zaheer"
print(max(text))
print(min(text))
srt=sorted(text)
print(srt)
srt=sorted(text,reverse=True)
print(srt)

# replace()
text="python&programming"
print(text.replace("&"," "))
