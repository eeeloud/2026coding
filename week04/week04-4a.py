# week04-4a.py (重寫week04-2.py)
# LeetCode 1732. Find the Highest Altitude
# 找到最高的海拔高度 (一直加,就好了!!!)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0 # 一開始的高度是 0
        for gg in gain: # Python 的進階 for 迴圈寫法
            H += gg
            ans = max(ans, H)
        return ans
