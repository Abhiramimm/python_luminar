cibil_score=int(input("Enter cibil score:")) #649

if cibil_score<550:
    print("Poor")
elif cibil_score>=550 and cibil_score<650: #649>=550 and 649<=650 True and True
    print("Average")
elif cibil_score >=650 and cibil_score<750:
    print("Good")
elif cibil_score>=750:
    print("Excellent")