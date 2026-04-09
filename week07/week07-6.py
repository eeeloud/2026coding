# week07-6.py 學習計畫 Stack 第3題,有點難
# Leetcode 649. Dota2 Senate
# Dota2 兩個陣營 「Radiant / 聖輝」和「Dire / 魔魘」照 senate 字串的順序出現
# 從左到右邊, 輪到的人, 可把「後面任一個敵對陣營」除掉。
# 輪完一輪, 繞到前面繼續, 直到全部字母都相同, 問最後「哪個陣營」得勝
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        banR, banD = 0, 0 # 目前等待「被消滅的次數」, 都還是0
        R, D = senate.count('R'), senate.count('D') # 目前各有幾個人?

        while queue: # 只要還有人在排隊, 就繼續進行「互相 Ban 對方」的遊戲
            now = queue.popleft() # 左邊吐出個字母, 他要消滅「敵對陣營」
            if now=='R':
                if banR > 0: # 已經紀錄要消滅1個人
                    banR -= 1 # 用掉1個消滅的名額
                    R -= 1 # 馬上少掉1個人
                else: # 你沒有被消滅, 太好了, 你可以過來反過來消滅對方
                    banD += 1
                    queue.append(now) # 再到最右邊排隊
            else: # now=='D'
                if banD > 0:
                    banD -= 1
                    D -= 1
                    continue
                else:
                    banR += 1
                    queue.append(now) # 再到最右邊排隊
            if R==0: return 'Dire' # 把 R 消滅光, 'D' 就得勝
            if D==0: return 'Radiant' # 把 D 消滅光, 'R' 就得勝
