"""
Question 3 Longest Substring Without Repeating Characters:
Given a string s, find the length of the longest 
substring without repeating characters.

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
"""
# Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a new Set
        charSet = set()
        # Set left pointer to first position
        l = 0 
        # Create Result var
        res = 0

        # Use Right pointer to loop through string
        for r in range(len(s)):
            # If right pointer is in the set remove the character at left pointer then increment left pointer position
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # Add the right pointer character to the set
            charSet.add(s[r])
            # compute window size for result
            res = max(res, r -l + 1)
        return res