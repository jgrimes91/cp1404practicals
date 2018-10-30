def build_it(n):
    if n > 0:
        return n + build_it(n-1)
    else:
        return 0

def add_it(n):
    return n + 1

print(build_it(6))
print(add_it(6))