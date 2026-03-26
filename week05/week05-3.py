# week05-3.py 厩策璸礶 Hash Table ( Map / Set )
# LeetCode 1207. Unique Number of Occurrences
# –贺计, 瞷Ω计ゲ斗常ぃ妓翅!
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr) # 参璸计瞷Ω计
        s = set() # ノㄓ瞷Ω计琌縒礚
        for c in  counter: # 盢计硋ㄓ
            # 代刚
            #print(c, counter[c]) # 计瞷碭Ω(痷Τ参璸!!)
            # 拜 counter[c] 琌常縒礚
            if counter[c] in s: # Τ瞷筁, ア毖
                return False
            s.add( counter[c] ) # 瞷硂瞷Ω计,  s 柑
        return True # 繦獽 return 
