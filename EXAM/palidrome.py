# longest palindromic substring
text="acadaad"
palindrome_list=[]

for i in range(len(text)):
    p,n=i,i  #p=i,n=i  p->previous, n->next, i->current
    # odd position
    while(p>=0 and n<len(text)) and text[p]==text[n]:
        palindrome_text=text[p:n+1]
        palindrome_list.append(palindrome_text)
        p-=1
        n+=1
    # even position
    p=i
    n=i+1
    while(p>=0 and n<len(text)) and text[p]==text[n]:
        palindrome_text=text[p:n+1]
        palindrome_list.append(palindrome_text)
        p-=1
        n+=1

def get_length(w):
    return len(w)
print(max(palindrome_list,key=lambda w:len(w)))