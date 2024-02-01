path="C:\\Users\\Admin\\Desktop\\mypython\\fileoperations\\worldcup.txt"

f=open(path,"r")
all_teams=[]


for line in f:
    cleaned_string=line.strip("\n")
    words=cleaned_string.split(" ")
    for w in words:
        if w.isalpha():
            all_teams.append(w)
print(set(all_teams))
wc={w:all_teams.count(w) for w in set(all_teams)}
print(wc)

# 2nd method

for lie in f:
    data=line.rstrip("\n").split(" ")
    all_teams.append(data[1])
print(set(all_teams))

wc={t:all_teams.count(t) for t in set(all_teams)}
print(wc)

value_key_list=[(v,k) for k,v in wc.items()]
print(max(value_key_list))
    

    

    
   

