from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        result = []
        counter = Counter(nums)

        for num, freq in counter.items():
            bucket[freq].append(num)

        for freq in range(len(bucket) -1, 0, -1): #range(start: optional, stop: required, step: optional)
            result.extend(bucket[freq])
            if len(result) == k:
                return result
        # return result[-k:]