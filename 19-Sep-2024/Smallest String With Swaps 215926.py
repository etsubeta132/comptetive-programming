# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        pairs.sort()
        parent = {i:i for i in range(len(s))}
        rank = {i:0 for i in range(len(s))}

        def find(x):
            while x != parent[x]:
                x = parent[x]
            
            return x
        
        def union(p1, p2):
            rootx = find(p1)
            rooty = find(p2)

            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx
                
                elif rank[rooty] < rank[rootx]:
                    parent[rootx] = rooty
                else:
                    parent[rootx] = rooty
                    rank[rooty] += 1 
        
        for pair in pairs:
            union(pair[0], pair[1])
        
        result = defaultdict(list)
        result2 = defaultdict(list)

        for key, val in parent.items():
            idx = find(val)
            result[idx].append(key)
            result2[idx].append(s[key])
        
        sorted_s = [""]*len(s)
        for res in result.keys():
            index = result[res]
            index.sort()
            chars = result2[res]
            chars.sort()
            for i in range(len(index)):
                sorted_s[index[i]] = chars[i]
        
        return "".join(sorted_s)
