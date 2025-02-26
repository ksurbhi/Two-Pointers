class Solution:
  # Method 1: Time Comp: O(n)
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        print(newStr)
        return newStr == newStr[::-1]



class Solution:
    #Method 2: Using 2 pointer
    # Time Comp: O(n)
    # Space: O(1)
    def isPalindrome(self, s: str) -> bool:
        start =0
        end = len(s)-1
        while start < end:
            while start < end and not s[start].isalnum():
                start +=1
            while end > start and not s[end].isalnum():
                end -=1
            if s[start].lower() != s[end].lower():
                return False
            start +=1
            end -=1
        return True 
