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
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
        return res
            
            
            