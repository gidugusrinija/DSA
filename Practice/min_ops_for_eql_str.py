"""
we will have two stings: st1, st2

we need to find minimum number of operations( insert, delete, replace) to make st1 into st2
"""

# approach: Tabulation

st1 = "abcef"
st2 = "acbcd"


def min_ops(st1, st2):

    m, n = len(st1), len(st2)

    # initialize 2D DP array

    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i

    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if st1[i-1] == st2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    return dp[m][n]


print(min_ops(st1, st2))


# approach: memoization

def min_ops_memo(st1, st2):

    memo = {}
    def find_ops(i, j):

        # base case

        if i == 0:
            # need to j elements
            return j
        if j == 0:
            # need to delete i elements
            return i

        # check for answer if already present

        if (i, j) in memo:
            return memo[(i, j)]

        if st1[i-1] == st2[j-1]:
            memo[(i, j)] = find_ops(i-1, j-1)

        else:

            insert = find_ops(i, j-1)
            delete = find_ops(i-1, j)
            replace = find_ops(i-1, j-1)

            memo[(i, j)] = min(insert, delete, replace) + 1

        return memo[(i, j)]

    return find_ops(len(st1), len(st2))



print(min_ops_memo(st1, st2))


