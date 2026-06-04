# week15-3.py 學習計劃 DP - Multidimensional 第3題
# LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def helper(i, hasStack): # 現在考慮 prices[i] 手上有 hasStack 股票嗎?
            if i==len(prices): return 0 # 終止條件
            # 手上有股票, 可以考慮「要不要賣」 賣的時候, 要再付手續費 fee
            if hasStack: ans = prices[i] + helper(i+1, False) - fee # 得到錢 prices[i]
            # 手上沒有股票, 可以考慮「要不要買」
            else: ans = -prices[i] + helper(i+1, True) # 花了錢 prices[i] 得到股票
            # 不買、也不賣
            return max( ans, helper(i+1, hasStack) )# 狀態相同, 直接換下一天

        return helper(0, False) # 從第0天開始思考, 手上沒有 股票
