class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = 0
        tracker = set(nums)

        for num in tracker:
            if num - 1 not in tracker:
                seq = num
                count = 1
                while seq + 1 in tracker:
                    count += 1
                    seq += 1

                record = max(count, record)

        return record
