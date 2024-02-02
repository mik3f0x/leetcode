class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
                
        res = [""] * numRows
        x = 1 if numRows > 2 else 0
        up = True
        i, j = 0, 0
        while i < len(s):
            if i > x and i % (numRows-1) == 0:
                up = not up
            res[j] += s[i]
            if up:
                j += 1
            else:
                j -= 1
            i += 1

        return ''.join(res)

print(Solution().convert("PAYPALISHIRING", 3))
print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("A", 1))
print(Solution().convert("AB", 1))
print(Solution().convert("ABCDEFGH", 2))
print(Solution().convert("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5))
