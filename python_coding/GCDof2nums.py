def gcd(n1, n2):
    x = max(n1, n2)
    y = min(n1, n2)
    while y != 0:
        x, y = y, x % y
    return x

result = gcd(48, 18)
print(result)