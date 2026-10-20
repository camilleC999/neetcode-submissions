class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        O(n^2) time complexity and space O(1)
        This jawn is not sorted. Won't matter though bc once we sort,
        that's a O(n log n) which is bettr than O(n^2) that we're gonna take.
        We don't care about indices
        '''
        res = []
        nums.sort()

        for base in range(len(nums) - 1, 1, -1):
            if base + 1 < len(nums) and nums[base] == nums[base + 1]:
                continue
            
            left, right = 0, base -1
            tgt = -nums[base]
            
            while left < right:
                total = nums[left] + nums[right]
                if total > tgt:
                    right -= 1
                elif total < tgt:
                    left += 1
                elif total == tgt :
                    res.append([nums[base], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res

        