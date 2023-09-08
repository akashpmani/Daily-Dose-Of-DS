"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result=""
        for i in range( max(len(a),len(b))):
            aBit = int( a[len(a)-1-i] ) if len(a)-1-i >=0 else 0
            bBit = int( b[len(b)-1-i] ) if len(b)-1-i >=0 else 0
            sum = aBit + bBit + carry
            if sum  >=2:
                carry = 1
                sum =  (sum)%2
            else:
                carry =0
            result = str(sum) + result
        if carry:return "1"+result
        return result
        
        
