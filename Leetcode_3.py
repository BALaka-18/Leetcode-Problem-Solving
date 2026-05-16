# Leetcode 3: Longest Substring with no repeating characters
# Sliding-Window

'''
Example:
s = "abcabcbb"
ans = 3

s = "pwwkew"
ans = 3

s = "tmmzuxt"
ans = 5
'''

def lengthOfLongestSubstring(s: str) -> int:
        hashMap = {}
        max_length = 0
        left = 0
        N = len(s)

        for right in range(N):
            hashMap[s[right]] = 1 + hashMap.get(s[right], 0)

            while hashMap[s[right]] > 1:
                hashMap[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, (right - left) + 1)

        return max_length