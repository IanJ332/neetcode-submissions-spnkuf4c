class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base = 0
        may_save = 0
        max_save = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]
            else:
                may_save += customers[i]
            
            if i >= minutes and grumpy[i - minutes] == 1:
                may_save -= customers[i - minutes]   

            max_save = max(may_save, max_save)
        
        return base + max_save