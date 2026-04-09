# week07-3.py 學習計畫 Stack 第1題
# Leetcode 2390. Removing Stars From a String
# 字串裡,每次讀到 '*' 星號 ,就要「再刪掉前1個字」
class Solution:
    def removeStars(self, s: str) -> str:
        ans = [] # 用來放答案的陣列 list 其實有 stack 的性質
        for c in s: # 逐一取出字母 c 再判斷
            if c =='*': ans.pop() # 遇到星號,吐掉1個字母
            else: ans.append(c) # 把不是星號的字母, 塞進去
        return ''.join(ans) # 用 單單.join()把陣列 join 成字串
