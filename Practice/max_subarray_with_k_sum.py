"""
l = [1, -2, 3, 4, -6, 5, -7, 1, 7]
target = 5


"""

def max_subarr(l, t):

    sum_map = {0: -1}
    max_len = 0
    prefix_sum = 0
    s, e = -1, -1

    for idx, num in enumerate(l):
        prefix_sum += num

        new_sum = prefix_sum - t

        if new_sum in sum_map:
            curr_len = idx - sum_map[new_sum]

            if max_len < curr_len:
                max_len = curr_len
                s, e = sum_map[new_sum], idx

        if prefix_sum not in sum_map:
            sum_map[prefix_sum] = idx

    return max_len, s+1, e+1

l = [1, -2, 3, 4, -6, 5, -7,1, 7]
t = 5

max_len, s, e = max_subarr(l, t)

print(max_len, s, e, l[s:e])




