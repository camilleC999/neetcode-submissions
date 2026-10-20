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
        up = len(nums) -1
        while up > 1:

            if up + 1 < len(nums) and nums[up] == nums[up + 1]:
                up -= 1
                continue

            left, right = 0, up - 1
            tgt = - nums[up]
            while left < right:
                total = nums[left] + nums[right]
                if total == tgt:
                    res.append([nums[up], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                elif total < tgt:
                    left += 1
                elif total > tgt:
                    right -= 1 

            up -= 1


        return res

        