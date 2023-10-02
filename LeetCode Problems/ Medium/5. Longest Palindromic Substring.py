class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        n = len(s)
        # Create a 2D table to store whether a substring is a palindrome or not.
        # dp[i][j] will be True if s[i:j+1] is a palindrome.
        dp = [[False] * n for _ in range(n)]

        start = 0  # Start index of the longest palindromic substring found so far.
        max_length = 1  # Length of the longest palindromic substring found so far.

        # All substrings of length 1 are palindromes.
        for i in range(n):
            dp[i][i] = True

        # Check for substrings of length 2.
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2

        # Check for substrings of length greater than 2.
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of the current substring.
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length

        return s[start:start + max_length]
