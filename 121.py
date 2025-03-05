class Solution:
    @classmethod
    def maxProfit(self, prices: list[int]) -> int:
        menor = prices[0]
        maximo_profit=0
        for i in prices[1:]:
            if menor>i:
                menor=i
            else:
                profit=i-menor
                if profit>maximo_profit:
                    maximo_profit=profit
        return maximo_profit

prices = [7,1,5,3,6,4]
print(Solution.maxProfit(prices))