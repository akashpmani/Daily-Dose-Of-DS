"""

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.

"""

#solution 1   using rotating elements

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        diff = 0
        while diff < len(s):
            if s == goal:
                return True
            s = s[1:] + s[:1]
            diff += 1

        return False
      
# Solution 2 if the conditions has to statisfy the goal must have to be in S+S because thier difference is only one element

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)
