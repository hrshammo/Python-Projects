class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the input list in ascending order.
        result = []  # Initialize an empty list to store the quadruplets.

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values of i.

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicate values of j.

                left, right = j + 1, len(nums) - 1  # Initialize two pointers.

                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicate values of left and right.
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1

        return result
