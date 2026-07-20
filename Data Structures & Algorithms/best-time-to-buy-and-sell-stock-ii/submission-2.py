class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        #Buy Once u reach min in a valley 
        # Sell When next wave is decreasing 
        profit = 0
        bought = 0
        onBuy = True 
        for i in range(n):
            if i + 1 < n:
                if onBuy is False:
                    # wants to sell 
                    if prices[i] >= bought and prices[i+1] < prices[i]:
                        profit += prices[i] - bought
                        bought = 0
                        onBuy = True

                else:
                    if prices[i+1] > prices[i]:
                        bought = prices[i]
                        onBuy = False
            else:
                if onBuy is False:
                    profit += prices[i] - bought
        return profit
            
