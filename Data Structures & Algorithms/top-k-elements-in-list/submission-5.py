from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        counter = Counter(nums)
        res = []

        if not nums:
            return res

        for key, val in counter.items():
            buckets[val].append(key)

        for freq in range(len(nums), 0, -1):
            bucket = buckets[freq]
            if not bucket:
                continue
            idx = 0
            while k > 0 and idx < len(bucket):
                res.append(bucket[idx])
                idx += 1
                k -= 1

            if k == 0:
                return res 

        return res
            
            
            