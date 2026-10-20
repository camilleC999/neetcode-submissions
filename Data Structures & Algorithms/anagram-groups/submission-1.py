from collections import Counter, defaultdict
from sortedcontainers import SortedDict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mother_hash = defaultdict(list)
        for s in strs:
            counter = Counter(s)
            c_set = tuple(SortedDict(counter).items())
            mother_hash[c_set].append(s)

        print(mother_hash)
        return list(mother_hash.values())
