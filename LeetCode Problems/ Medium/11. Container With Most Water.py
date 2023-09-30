class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the width (difference between indices)
            width = right - left
            # Calculate the height (minimum height between left and right pointers)
            h = min(height[left], height[right])
            # Calculate the current area
            area = width * h
            # Update max area if the current area is greater
            max_area = max(max_area, area)

            # Move the pointers inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
