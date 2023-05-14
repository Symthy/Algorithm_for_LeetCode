class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = {}
        longest = 0
        length = 0
        for c in s:
            if c in substrings:
                if longest < length:
                    longest = length
                length = 0
                substrings = {}
            substrings[c] = ""
            length += 1
        return longest if length < longest else length
