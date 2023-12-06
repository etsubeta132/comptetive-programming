class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        least_idx = float('inf')
        common_str = {}
        least_index_sum = []

        for string in list1:
            if string in list2:
                index_sum = list1.index(string)+list2.index(string)
                common_str[string] = index_sum
                least_idx = min(least_idx,index_sum)

        for string in common_str:
            if common_str[string]==least_idx:
                least_index_sum.append(string)
        return least_index_sum


        