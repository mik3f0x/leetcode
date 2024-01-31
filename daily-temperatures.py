from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        scale = [len(temperatures)*2] * 102

        for i in range(len(temperatures)-1, -1, -1):
            scale[temperatures[i]] = i
            val = min(scale[temperatures[i]+1:]) - i
            temperatures[i] = val if val < len(temperatures) else 0

        return temperatures 


print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
print(Solution().dailyTemperatures([30,40,50,60]))
print(Solution().dailyTemperatures([30,60,90]))
print(Solution().dailyTemperatures([70]))
print(Solution().dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
