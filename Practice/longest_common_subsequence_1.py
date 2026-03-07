# Approach: memoization

"""
1. uses recursion
2. comparison starts from end of the words
3. use memoization to store results before returning the answer
4. define base case: i.e., if either of the string is completely explored, return 0 because there is nothing matched
5. check if answer is already exist for len of words before calculating
6. if present, return answer directly else calculate
"""

st1 = "abc"
st2 = "acbcd"


def lcs_memo(st1, st2):
    memo = {}

    def find_lcs(i, j):
        # Base case
        if i == 0 or j == 0:
            return 0

        # find if answer already exists
        if (i, j) in memo:
            return memo[(i, j)]

        if st1[i - 1] == st2[j - 1]:

            memo[(i, j)] = 1 + find_lcs(i - 1, j - 1)

        else:
            memo[(i, j)] = max(find_lcs(i - 1, j), find_lcs(i, j - 1))

        return memo[(i, j)]

    return find_lcs(len(st1), len(st2))


# if we want to know the subsequence change the return type (str)

def lcs_memo_new(st1, st2):
    memo = {}

    def find_lcs_new(i, j):
        # Base case
        if i == 0 or j == 0:
            return ""

        # find if answer already exists
        if (i, j) in memo:
            return memo[(i, j)]

        if st1[i - 1] == st2[j - 1]:

            memo[(i, j)] = find_lcs_new(i - 1, j - 1) + st1[i - 1]

        else:
            res1 = find_lcs_new(i - 1, j)
            res2 = find_lcs_new(i, j - 1)
            memo[(i, j)] = res1 if len(res1) > len(res2) else res2

        return memo[(i, j)]

    return find_lcs_new(len(st1), len(st2))


print(lcs_memo(st1, st2))
print(lcs_memo_new(st1, st2))
