from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1:
            return [str(nums[0])]

        res = []
        hold = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if hold == i-1:
                    res.append(str(nums[i-1]))
                else:
                    res.append(f"{nums[hold]}->{nums[i-1]}")
                hold = i
            if i == len(nums)-1:
                if hold == i:
                    res.append(str(nums[i]))
                else:
                    res.append(f"{nums[hold]}->{nums[i]}")

        return res



print(Solution().summaryRanges([0,1,2,4,5,7]))
print(Solution().summaryRanges([0,2,3,4,6,8,9]))
print(Solution().summaryRanges([1]))
print(Solution().summaryRanges([]))


# 6:40