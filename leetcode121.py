class Solution():
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        
        return profit
    
a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))
print(a.maxProfit([7,6,4,3,1]))
