from typing import List
from collections import defaultdict


class Solution:
    # with Single hash method
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for str in strs:
            hash = [0] * 26
            str = str.lower()
            for i in str:
                hash[ord(i) - ord('a')] += 1
            result[tuple(hash)].append(str)
        return result.values();


soln = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(soln.groupAnagrams(strs))
