from typing import List
#Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        common_prefix = strs[0]

        for string in strs[1:]:
            i = 0
            while i < len(common_prefix) and i < len(string) and common_prefix[i] == string[i]:
                i += 1

            common_prefix = common_prefix[:i]

            if not common_prefix:
                break

        return common_prefix
