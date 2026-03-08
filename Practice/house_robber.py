l = [1,2,3,1]

def max_rob_memo(l):
    memo = {}
    def solve(i):
        if i >= len(l):
            return 0

        if i in memo:
            return memo[i]

        pick = l[i] + solve(i+2)

        non_pick = solve(i+1)

        memo[i] = max(pick, non_pick)

        return memo[i]
    return solve(0)


def max_rob_tabular(l):
    n = len(l)
    dp = [0] * (n+2)

    for i in range(n-1, -1, -1):
        pick = l[i] + dp[i+2]
        non_pick = dp[i+1]
        dp[i] = max(pick, non_pick)
    return dp[0]

print(max_rob_memo(l))
print(max_rob_tabular(l))
