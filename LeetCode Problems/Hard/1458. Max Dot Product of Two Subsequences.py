class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        
        # Create a 2D dp array to store the maximum dot product
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # Calculate the current dot product
                current_product = nums1[i - 1] * nums2[j - 1]
                
                # Update the dp array by choosing the maximum of the following options:
                # 1. The previous dot product dp[i-1][j-1] plus the current product.
                # 2. The current product itself.
                # 3. The maximum dot product without the current element from either array.
                dp[i][j] = max(current_product, current_product + dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        
        # The result is stored in dp[n][m]
        return dp[n][m]
