text="#orange color wow #yellow color wow #blue color wow"

words=text.split(" ")

for w in words:
     if w.startswith("#"):
         print(w)
    

