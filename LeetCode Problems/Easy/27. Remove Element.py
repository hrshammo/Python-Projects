class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Initialize the count of elements to keep

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
