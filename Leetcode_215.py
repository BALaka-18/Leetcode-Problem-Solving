# Leetcode 215: Kth Largest Element in an Array
# Min-Heap/Priority Queue

'''
Example: nums = [3, 2, 1, 5, 6, 4], k = 2
ans = 5
'''

import heapq    # For min-heap

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        N = len(nums)
        min_heap = []
        heapq.heapify(min_heap) # List -> min heap

        for i in range(N):
            if len(min_heap) < k:
                heapq.heappush(min_heap, nums[i])   # Keep adding till threshold is reached
            else:
                heapq.heappushpop(min_heap, nums[i])    # Once threshold is reached, keep popping the smallest element in the heap, so we know the remaining k elements in the heap are the k largest elements in the original list.
        
        return min_heap[0]
        