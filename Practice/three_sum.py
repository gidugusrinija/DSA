"""
l = [1, 0, -2, -6, 5, 4, 3, 9]
t = 3

approach:

1. sort the array
2. fix the i and search j, k to make final sum.
3. if don't find the sum, increment i
"""

l = [1, 0, -2, -6, 5, 4, 3, 9]
t = 3

def three_sum(l, t):

    i = 0

    sorted_l = sorted(l)
    print(sorted_l)
    n = len(sorted_l)
    while i < len(l)-2:

        j = i + 1
        k = n - 1

        reqd_sum = t - sorted_l[i]
        while j < k:
            curr_sum = sorted_l[j] + sorted_l[k]

            if curr_sum == reqd_sum:
                return (i, j, k)
            if curr_sum > reqd_sum:
                k -= 1
            else:
                j += 1

        i += 1


print(three_sum(l, t))
