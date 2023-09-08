# Leetcode easy problem: 1822. Sign of the Product of an Array
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        num_negatives = 0
        num_zeros = 0

        for num in nums:
            if num == 0:
                num_zeros += 1
            elif num < 0:
                num_negatives += 1

            product *= num

        if num_zeros > 0:
            return 0
        elif num_negatives % 2 == 0:
            return 1
        else:
            return -1
