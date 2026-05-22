# Leetcode 973. K closest points to Origin
# Max-heap

'''
Example: points = [[3, 3], [5, -1], [-2, 4]], k = 2
ans = [[3, 3], [-2, 4]]
'''

import heapq    # For min heap
import collections  # For hashmap
import numpy as np  # For Euclidean distance

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashMap = collections.defaultdict(int)
        for point in points:
            dist = np.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            hashMap[dist] = point
        
        max_heap = []
        heapq.heapify(max_heap)

        for p in points:
            # Use max-heap logic
            d = -np.sqrt((p[0] - 0)**2 + (p[1] - 0)**2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (d, p))
            else:
                heapq.heappushpop(max_heap, (d, p))

        return [elem[1] for elem in max_heap]
        