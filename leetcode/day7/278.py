# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        
        while start <= end:
            center = start + int((end - start) / 2)
            if(isBadVersion(center)):
                end = center - 1
            else:
                start = center + 1
                
        return start 
        
        
        
            