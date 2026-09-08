class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalpha() or c.isdigit())
        copied_s = s
        reversed_s = s[::-1]
        if copied_s == reversed_s:
            return True
        else:
            return False    
      