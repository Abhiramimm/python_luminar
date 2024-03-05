# def greeting_dec(fn):
#     def wrapper(name):
#         txt="hello coder"
#         return fn(name)
#     return wrapper

def greeting_dec(fn):
    def wrapper(name):
        result=fn(name)
        return f"hello programmer {result}"
    return wrapper



@greeting_dec
def morning_greeting(name):
    return f"{name} good morning"

@greeting_dec
def afternoon_greeting(name):
    return f"{name} good afternoon"

print(morning_greeting("john"))
print(afternoon_greeting("john"))