# user defined decorator

def swap_dec(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper

@swap_dec
def sub(n1,n2):
    return n1-n2
print(sub(5,10))