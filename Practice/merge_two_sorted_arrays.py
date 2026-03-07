l1 = [-1, 3, 4, 8, 0, 0, 0]

l2 = [2, 7, 9]

m = len(l1)
n = len(l2)
list_p = m - 1
s1 = m - n - 1

s2 = n - 1

while s2 >= 0:
    if l1[s1] > l2[s2]:
        l1[list_p] = l1[s1]
        s1 -= 1
    else:
        l1[list_p] = l2[s2]
        s2 -= 1
    list_p -= 1

print(l1)