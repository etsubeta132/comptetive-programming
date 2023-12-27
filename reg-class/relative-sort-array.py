class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        arr2_dict = {arr2[i]:i for i in range(len(arr2))}
        
        size = len(arr1)

        for i in range(size):
            
            if arr1[i] not in arr2_dict:
                arr2_dict[arr1[i]] = len(arr1) + arr1[i]
            min_num = arr2_dict[arr1[i]]
            p =i

            for j in range(i+1,size):

                if arr1[j] not in arr2_dict:
                    arr2_dict[arr1[j]] = len(arr1) + arr1[j]
                    
                idx = arr2_dict[arr1[j]]
                if min_num > idx:
                    min_num = idx
                    p = j
                    
            
            arr1[i],arr1[p] = arr1[p],arr1[i]
        
        return arr1