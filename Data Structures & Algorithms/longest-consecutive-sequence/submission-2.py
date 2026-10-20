class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        truth = set(nums)
        record = 0

        for i in truth:
            if i - 1 not in truth:
                length = 0
                cur = i
                while cur in truth:
                    length += 1
                    cur += 1
                
                record = max(record, length)
                

        return record
