class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}

        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        for key, val in dic.items():
            if val == 1:
                return s.index(key)

        return -1
    

print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))
print(Solution().firstUniqChar("a"))
