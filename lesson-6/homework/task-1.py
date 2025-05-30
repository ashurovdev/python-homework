def check(func):
    def wrapper(a,b):
        if b==0:
            return f'b nolga(0) teng bo\'lishi mumkin emas'
        return func(a,b)
    return wrapper

@check
def div(a,b):
    return a/b

print(div(10,2))