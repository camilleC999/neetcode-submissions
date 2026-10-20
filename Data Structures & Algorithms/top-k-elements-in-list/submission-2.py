import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        result = []
        counter = Counter(nums)
        for i, j in counter.items():
            bucket[j].append(i)

        for freq in bucket:
            result.extend(freq)

        return result[-k:]