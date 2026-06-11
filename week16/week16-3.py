# week16-3.py 學習計劃 Intervals 第1題
# LeetCode 435. Non-overlapping Intervals
# 要刪掉幾個「區段」才能夠「都不重疊」
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #intervals.sort() # 先排序, 依據 右邊的結束時間
        intervals.sort( key = lambda x:x[1] ) # 用右邊的end大小來排序
        ans = 0
        previous_end = -inf #很左邊、遠的「負無限大」先不限制
        for start, end in intervals: # 逐一取出 [start, end]
            if previous_end <= start: # 沒有重疊
                previous_end = end # 更新, 現在 end 的時間
            else: # 糟了! 竟然重疊! 「現在這段」不能用!!!
                ans += 1 # 要把「現在這段」刪掉
        return ans
