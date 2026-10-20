class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for base in range(len(nums) - 2):
            if base > 0 and nums[base] == nums[base - 1]:
                continue
            tgt = - nums[base]
            left, right = base + 1, len(nums) - 1
            while left < right:
                diff = nums[left] + nums[right]
                if diff == tgt:
                    res.append([nums[base], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif diff > tgt:
                    right -= 1
                elif diff < tgt:
                    left += 1

        return res



        