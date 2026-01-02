"""
14. Longest Common Prefix
Easy
Topics
premium lock icon
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

strs = ["dog","racecar","car"]

def longest_common_prefix(strs):
    res = ""
    min_str = min(strs)
    max_str = max(strs)
    for i in range(len(min_str)):
        if min_str[i] != max_str[i]:
            return res
        if min_str[i] == max_str[i]:
            res += min_str[i]
    return res

res = longest_common_prefix(strs)
print(res)
