import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        counter = Counter(nums)
        for i, j in counter.items():
            heapq.heappush(max_heap, (-j, i))
        
        return [heapq.heappop(max_heap)[1] for i in range(k)]