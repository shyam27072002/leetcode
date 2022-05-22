"""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned)."""

class Solution(object):
    def reverse(self, x):
       sign=1
       if(x<0):
              n=-1*x
              sign =-1
       else:
              n=x
       res=0
       while(n>0):
              res = (res*10)+(n%10)
              n=n//10
       res= sign*res
       if(res<(-1*(2**31)) or res>((2**31)-1)):
            return 0
       return res
   
"""Runtime: 32 ms, faster than 36.12% of Python online submissions for Reverse Integer.
Memory Usage: 13.5 MB, less than 13.71% of Python online submissions for Reverse Integer."""
