def gen(n):
    i = 0
    while i < n:
        yield i
        i += 1

print(gen(5))
