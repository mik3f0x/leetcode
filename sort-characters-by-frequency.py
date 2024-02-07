class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}

        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        res = ''
        for key, value in sorted(dic.items(), key=lambda item: item[1], reverse=True):
            res += key * value

        return res
    

print(Solution().frequencySort("tree"))
print(Solution().frequencySort("cccaaa"))
print(Solution().frequencySort("Aabb"))
