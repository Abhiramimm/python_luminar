lst=[10,20,20,40,50,20]
#10,20,40,50
st=set(lst)
print(st)

all_users={"sachin","dravid","laxman","jadeja","dhoni","raina"}
dhoni_friends={"sachin","raina"}

#dhoni suggestions -> dravid,laxman,jadeja
suggestions_set=all_users.difference(dhoni_friends)
suggestions_set.discard("dhoni")
print(suggestions_set)


