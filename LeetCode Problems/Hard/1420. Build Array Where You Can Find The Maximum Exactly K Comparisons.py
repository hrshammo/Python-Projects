class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # Create a memoization table with dimensions (pos, max_val, comparisons).
        memo = {}

        # Define a recursive function with memoization.
        def dp(pos, max_val, comparisons):
            if comparisons > k:
                return 0
            if pos == n:
                return 1 if comparisons == k else 0

            if (pos, max_val, comparisons) in memo:
                return memo[(pos, max_val, comparisons)]

            ans = 0
            for num in range(1, m + 1):
                if num > max_val:
                    ans += dp(pos + 1, num, comparisons + 1)
                else:
                    ans += dp(pos + 1, max_val, comparisons)
                ans %= MOD

            memo[(pos, max_val, comparisons)] = ans
            return ans

        return dp(0, 0, 0)
