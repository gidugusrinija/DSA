# Approach: Tabulation

"""
Approach:
1. comparison starts at beginning
2. bottom - up approach
3. uses iteration to fill the dp table
4. uses 2D- array for DP
5. fill column 0 and row 0 with all 0's why because there is absolutely no match (empty str)
6. if characters match, fill 1 + diagonal value
7. if not fill with max(top, left)
"""

st1 = "abc"
st2 = "acbcd"


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

    # In order to get subsequence, do back tracking

    idx1, idx2 = m, n
    res = []

    while idx1 > 0 and idx2 > 0:

        if st1[idx1 - 1] == st2[idx2 - 1]:
            res.append(st1[idx1 - 1])
            idx1 -= 1
            idx2 -= 1

        else:
            if dp[idx1 - 1][idx2] > dp[idx1][idx2 - 1]:
                idx1 -= 1
            else:
                idx2 -= 1

    print("".join(reversed(res)))

    return dp[m][n]


print(lcs_tabulation(st1, st2))
