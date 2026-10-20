class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        truth = set(nums)
        record = 0

        while truth:
            lg_nm = max(truth)
            track = lg_nm - 1
            truth.discard(lg_nm)
            cur = 1
            while track in truth:
                cur += 1
                truth.discard(track)
                track -= 1

            if cur > record:
                record = cur

        return record



                
        