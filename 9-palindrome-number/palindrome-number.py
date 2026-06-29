class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        num1=0
        while num>0:
            num1=num1*10+num%10
            num//=10
        
        if num1== x:
            return True
        else:
            return False