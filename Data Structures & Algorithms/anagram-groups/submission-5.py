from collections import Counter, defaultdict
from sortedcontainers import SortedDict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mother_hash = defaultdict(list)
        for word in strs:
            count = SortedDict(Counter(word))
            mother_hash[tuple(count.items())].append(word)
            print(count)

        print(mother_hash)
        return [mother_hash[i] for i in mother_hash]
