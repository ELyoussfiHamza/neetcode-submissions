class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        
        finish_at = customers[0][0]
        wait = 0
        for arr , tm in customers:
            if arr < finish_at:
                wait += finish_at - arr + tm
                finish_at = finish_at + tm
            else:
                wait += tm
                finish_at = arr + tm
            
             
        return wait/n

        

