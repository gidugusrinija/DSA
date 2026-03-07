"""
we will have two stings: st1, st2

we need to find minimum number of operations( insert, delete) to make st1 into st2
"""

st1 = "abcef"
st2 = "acbcd"

# the result will len(st1+st2) - (2 * lcs)


def lcs_tabulation(st1, st2):

    m, n = len(st1), len(st2)

    # Create DP 2-D array
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):

            if st1[i-1] == st2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


res = len(st1+st2) - (2 * lcs_tabulation(st1, st2))

print(res)

