# Leetcode 153: Find Minimum in Rotated Sorted Array
# Modified Binary Search

'''
Example: 
arr = [4, 5, 6, 7, 0, 1, 2]
res = 0

'''

def findMin(nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right -= 1
            else:
                left += 1

        return nums[mid]