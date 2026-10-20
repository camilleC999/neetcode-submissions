from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
        res = []

        for num, freq in count.items():
            bucket[freq].append(num)


        for i in range(len(bucket) -1, 0, -1):
            if not bucket[i]:
                continue
            
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

            
            
            