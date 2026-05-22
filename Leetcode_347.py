# Leetcode 347: Top K Frequent Elements
# Min-heap

'''
Example: nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k =2
ans = [1, 2]
'''

import heapq    # For min heap
import collections  # For frequency hashmap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        hashMap = collections.Counter(nums)

        min_heap = []
        heapq.heapify(min_heap)

        for key, value in hashMap.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (value, key))
            else:
                heapq.heappushpop(min_heap, (value, key))
        
        return [elem[1] for elem in min_heap]