class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[right].isalnum() and s[left].isalnum():
                if s[right].lower() != s[left].lower():
                    return False
                else: 
                    right -= 1
                    left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                left += 1



        return True