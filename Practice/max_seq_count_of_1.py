l = "00111100000011111110000011"

c = 0

max_len = 0

s, e = -1, -1

for idx, i in enumerate(l):
    if i == "1":
        c += 1
    else:
        c = 0
    if c > max_len:
        max_len = c
        s, e = idx-c+1, idx

    max_len = max(max_len, c)

print(max_len, s, e)
