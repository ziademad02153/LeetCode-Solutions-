class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)
        if n == 0 or k == 0:
            return 0
            
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit
            
        buy = [-(1 << 31)] * (k + 1)
        sell = [0] * (k + 1)
        
        for price in prices:
            for j in range(1, k + 1):
                candidate_buy = sell[j - 1] - price
                buy[j] = buy[j] if buy[j] > candidate_buy else candidate_buy
                
                candidate_sell = buy[j] + price
                sell[j] = sell[j] if sell[j] > candidate_sell else candidate_sell
                
        return sell[k]