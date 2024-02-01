orders=["tea","tea","coffe","tea","vb","cb","cb","vb"]

wc={o:orders.count(o) for o in set(orders)}
print(wc)

