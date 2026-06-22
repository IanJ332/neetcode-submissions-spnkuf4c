class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_sorted = sorted(s1)
        
        i = 0
        while i <= len(s2) - len(s1):
            if s2[i] in s1:
                s3 = s2[i : i + len(s1)]
                if sorted(s3) == s1_sorted:
                    return True
            i += 1
            
        return False