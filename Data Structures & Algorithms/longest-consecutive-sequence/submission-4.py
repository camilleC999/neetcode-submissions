class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = 0
        for i in nums:
            if i - 1 not in nums:
                cur = i
                ct = 1
                while cur + 1 in nums:
                    ct += 1
                    cur += 1
                record = max(record, ct)
        
        return record


