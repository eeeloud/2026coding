# week14-2a.py 學習計劃 DP - 1D 第1題 Easy題
# LeetCode 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1] + [0] * n
        for i in range(3 ,n+1):
            a[i] = a[i-1] + a[i-2] + a[i-3]
        #print(a)
        return a[n]

        if n==0: return 0
        if n==1: return 1
        if n==2: return 1
        if n==3: return 4
        if n==4: return 7
        if n==5: return 13
        if n==6: return 24
        if n==7: return 44
        if n==8: return 81
        if n==9: return 149
        if n==10: return 274
