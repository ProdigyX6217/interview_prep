class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_s = s.reverse()
        if s == reversed_s:
            return True
        else:
            return False

result1 = Solution().isPalindrome("racecar")
print(result1)