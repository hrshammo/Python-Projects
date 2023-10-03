class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Create a dictionary to store the count of each number.
        num_counts = {}
        good_pairs = 0

        # Count the occurrences of each number in nums.
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1

        # Calculate the number of good pairs for each number.
        for count in num_counts.values():
            good_pairs += count * (count - 1) // 2

        return good_pairs
