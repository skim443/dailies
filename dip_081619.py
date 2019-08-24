# Given a string, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        # winner could be the entire string if no repeats
        longest_str = s

        cand = ""
        for idx, char in enumerate(s):
            cand += char
            # at 2nd character and beyond, start comparing to previous character
            # if repeat, then compare length of candidate to current winner
            if idx > 0:
                if s[idx] == s[idx-1]:
                    if len(cand) > max_len:
                        max_len = len(cand)
                        # chop off last dupe
                        longest_str = cand[:-1]
                        # re-init cand
                        cand = char

        return len(longest_str)


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
