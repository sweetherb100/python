'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true
Example 2:
Input: "()[]{}"
Output: true
Example 3:
Input: "(]"
Output: false
Example 4:
Input: "([)]"
Output: false
Example 5:
Input: "{[]}"
Output: true
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dicmap = {'(': ')',
                  '[': ']',
                  '{': '}'}

        print(dicmap.keys())
        print(dicmap.values())
        stack = []  # FILO

        try:
            for i in range(len(s)):
                if s[i] in dicmap.keys():
                    stack.append(s[i])  # same as push
                if s[i] in dicmap.values():  # pop
                    if dicmap[stack.pop()] is not s[i]:
                        return False

        except:
            return False  # IndexError: pop from empty list (sth wrong at the end)

        if len(stack) != 0:  # (sth wrong at the front)
            return False

        return True
solution = Solution()
print(solution.isValid("([)]"))

'''
numlist=[1,2,3,4,5,6]
print(numlist.pop()) #6

wintable = { #the one infront can win the end
    'scissors':'paper',
    'rock':'scissors',
    'paper':'rock'
}
print(wintable['scissors']) #paper
'''