# Leetcode 17: Letter Combinations of a Phone Number
# Backtracking

'''
Example:
digits = "23"
res = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

'''

def letterCombinations(digits: str) -> List[str]:
        digit_to_letterMap = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        n = len(digits)
        res = []
        curr_path = []

        def backtrack(i):
            # Leaf condition - we've visited all digits in one path
            if i == n:
                res.append(''.join(curr_path))
                return
            
            for ch in digit_to_letterMap[digits[i]]:
                # Add case to current path
                curr_path.append(ch)
                # Call recursion for next edge
                backtrack(i + 1)
                # Backtrack
                curr_path.pop()
        
        backtrack(0)
        return res