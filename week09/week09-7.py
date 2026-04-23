# week09-7.py 學習計畫 Linked List 第2題 Medium 題
# LeetCode 2130. Maximum Twin Sum of a Linked List
# 問「頭尾相加」的組和,加起來「最大值」有多大?
# 頭尾「兩兩配在一起」 希望加起來最大
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []
        while head:
            a.append( head.val )
            head = head.next

        N = len(a)
        ans = 0
        for i in range(N):
            ans = max(ans, a[i]+a[N-1-i])
        return ans
