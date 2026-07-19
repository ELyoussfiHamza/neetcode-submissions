class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalnumm(v):
            return v.isalnum()
        alphanumeric = "".join(list(filter(isalnumm ,list(s))))
        print(alphanumeric)
        n = len(alphanumeric)
        left = 0
        right = n-1
        while (left<right):
            if (alphanumeric[left].upper()!=alphanumeric[right].upper()):
                return False
            left+=1
            right-=1
        return True


        