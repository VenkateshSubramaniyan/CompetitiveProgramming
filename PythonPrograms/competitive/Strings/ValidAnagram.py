class Solution:
    # with Single hash method
    def isAnagram(self, s: str, t: str) -> bool:
        hash = [0] * 26
        s = s.lower()
        t = t.lower()

        for i in s:
            hash[ord(i) - ord('a')] += 1

        for i in t:
            hash[ord(i) - ord('a')] -= 1
        for i in hash:
            if i != 0:
                return False
        return True


soln = Solution()
print(ord('a'))
print(soln.isAnagram("anagram", "nagaram"))
