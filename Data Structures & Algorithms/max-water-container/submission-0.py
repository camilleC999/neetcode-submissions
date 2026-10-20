class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        max_vol = 0
        while left < right: 
            vol = min(nums[left], nums[right]) * (right - left)
            max_vol = max(vol, max_vol)
            if nums[left] < nums[right]:
                left += 1 
            elif nums[left] > nums[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return max_vol
