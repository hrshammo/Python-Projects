class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # Define a recursive function to count the number of valid arrays.
        def dp(pos, max_val, comparisons):
            if comparisons > k:
                return 0
            if pos == n:
                return 1 if comparisons == k else 0

            ans = 0
            for num in range(1, m + 1):
                if num > max_val:
                    ans += dp(pos + 1, num, comparisons + 1)
                else:
                    ans += dp(pos + 1, max_val, comparisons)
                ans %= MOD

            return ans

        return dp(0, 0, 0)
