"""
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
 

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.

"""

class Solution:
    def toLowerCase(self, s: str) -> str:
        lowercase = ""
        for char in s:
            if ord(char) >= 65 and ord(char) <= 90:
                lowercase += chr(ord(char) + 32)
            else:
                lowercase += char
        return lowercase

# OR Using Inbuilt lower Function For solving it in one line of code

class Solution:
    def toLowerCase(self, s: str) -> str:
      return s.lower()

