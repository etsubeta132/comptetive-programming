class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        occ_25 = len(arr)/4
        num_count = Counter(arr)
        
        print(num_count)
        for key, value in num_count.items():
            if value > occ_25:
                return key
                break
            
        