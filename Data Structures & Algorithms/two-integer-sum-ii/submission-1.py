class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L, R = 0, len(nums) - 1

        while L < R:
            tgt = nums[L] + nums[R]

            if tgt > target:
                R -= 1
                while nums[R] == nums[R + 1]:
                    R -= 1
            elif tgt < target:
                L += 1
                while nums[L] == nums[L - 1]:
                    L += 1 
            else:
                return [L+1, R+1]    