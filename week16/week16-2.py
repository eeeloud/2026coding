# week16-2.py 學習計劃 Backtracking 第2題
# LeetCode 216. Combination Sum III
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        # i:現在試到哪個數? k:還要幾個數? n:還要補多少?
        def helper(now, i, k, n): # now:現在累積的數
            if k==0 and n==0: # 成功了!
                ans.append(now) # 就把 now 塞入ans 裡
            if k<0 or n<0: return # 走完「函式呼叫函式」, 終止!
            for ii in range(i, 10): # i...9 之間的數
                # 現在如果放入 ii
                helper(now + [ii], ii+1, k-1, n-ii)
                # 下次要試 ii+1, 用掉1個數, 總和少ii
        helper([], 1, k, n)
        return ans
