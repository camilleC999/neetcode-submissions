from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tt = defaultdict(int)

        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in tt:
                return [tt[tmp], i]
            else:
                tt[nums[i]] = i


