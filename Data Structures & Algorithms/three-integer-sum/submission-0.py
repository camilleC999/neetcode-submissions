class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        O(n^2) time complexity and space O(1)
        This jawn is not sorted. Won't matter though bc once we sort,
        that's a O(n log n) which is bettr than O(n^2) that we're gonna take.
        We don't care about indices
        '''
        res = set()
        nums.sort()
        print(nums)
        up = len(nums) -1
        while up > 1:
            left, right = 0, up - 1
            print(f"nums[up]: {nums[up]}")
            tgt = - nums[up]
            while left < right:
                print(f"left: {left}")
                print(f"right: {right}")
                total = nums[left] + nums[right]
                print(f"total: {total}")
                if total == tgt:
                    res.add((nums[left], nums[right], nums[up]))
                    left += 1
                    right -= 1
                elif total < tgt:
                    left += 1
                elif total > tgt:
                    right -= 1 

            up -= 1


        return [list(triplet) for triplet in res]

        