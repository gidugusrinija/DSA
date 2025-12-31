"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class LongestSubstring:
    def longest_substring(self, str1):
        visited_string = ""
        len_list = []
        i = 0
        j = i
        while j < len(str1):
            char = str1[j]
            if char not in visited_string:
                visited_string += char
                j = j + 1
            else:
                len_list.append(len(visited_string))
                visited_string = ""
                i = i + 1
                j = i
        return max(len_list + [len(visited_string)])


r = LongestSubstring().longest_substring("abcdeabcfdgh")
print(r)

#sliding window approach
class LongestSubstring:
    def longest_substring(self, str1):
        left = 0
        max_len = 0
        index_map = {}
        for right, value in enumerate(str1):
            if value in index_map and index_map[value] >= left:
                left = index_map[value] + 1
            index_map[value] = right
            max_len = max(max_len, right - left + 1)

        return max_len, str1[left: left + max_len]



#set based sliding window

class LongestSubstring:
    def longest_substring(self, str1):
        left = 0
        visited = set()
        max_len = 0

        for right in range(len(str1)):
            while str1[right] in visited:
                visited.remove(str1[left])
                left += 1
            visited.add(str1[right])
            max_len = max(max_len, right - left + 1)
        return max_len


