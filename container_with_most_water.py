from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max = 0

        while left < right:
            area = min(height[left], height[right]) * (right-left)

            if height[right] < height[left]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                right -= 1
                left += 1

            if max < area:
                max = area

        return max
    


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1,1]))
print(Solution().maxArea([1,8,8,1]))
print(Solution().maxArea([8,1,1,8]))