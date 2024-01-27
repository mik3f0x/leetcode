class Solution:
    def longestPalindrome(self, s: str) -> str:
        dic = {s[0]: 1}

        def getPalindrome(s, i, x):
            j, k = i, i+x
            temp = ''
            while j >= 0 and k < len(s) and s[j] == s[k]:
                temp = s[j:k+1]
                j -= 1
                k += 1
            dic[temp] = len(temp)

        for i in range(len(s)-1):
            if i+2 < len(s) and s[i] == s[i+2]:
                getPalindrome(s, i, 2)
            if i+1 < len(s) and s[i] == s[i+1]:
                getPalindrome(s, i, 1)

        return max(dic, key=dic.get)
    

print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("racecarddhgblabbalbfjgutublabbalbu"))
print(Solution().longestPalindrome("a"))
print(Solution().longestPalindrome("qmnlop"))
print(Solution().longestPalindrome("ccccc"))
