st = "aabcdbef"

left = 0
max_len = 0
visited_map = {}

for right, val in enumerate(st):

    if val in visited_map and visited_map[val] >= left:
        left = visited_map[val] + 1
    visited_map[val] = right

    max_len = max(max_len, right - left + 1)

print(max_len, st[left: left + max_len])
