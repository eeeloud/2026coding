# week08-4.py 學習計畫 Binary Search 第2題
# LeetCode 2300. Successful Pairs of Spells and Potions
# 想知某種 spells[i] 魔法, 配幾種藥水可以成功?
# 魔法師「施咒spell」配合「藥水potion」要乘起來
# spells[i] vs. potions[j] 希望乘起來後 >= success 值
# 但陣列很大, 不能暴力「全部都試乘一次」, 可 potions 先 sort 後, 再 binary search
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() # 藥水「小到大」排好
        P = len(potions) # 有 P 種藥水
        ans = []
        for spell in spells: # 每一種魔法, 都試一次
            now = P - bisect_left(potions, success/spell)
            ans.append(now) # 全部藥水P瓶 - 會失敗的藥水??瓶, 便是成功的藥水瓶數
        return ans
