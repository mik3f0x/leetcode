from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(0, len(nums)-2, 3):
            if nums[i+2] - nums[i] > k:
                return []
            else:
                res.append([nums[i], nums[i+1], nums[i+2]])

        return(res)


print(Solution().divideArray([1,3,4,8,7,9,3,5,1], 2))
print(Solution().divideArray([1,3,3,2,7,3], 3))