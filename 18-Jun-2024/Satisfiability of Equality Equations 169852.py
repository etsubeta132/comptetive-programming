# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        variables = set()

        for variable in equations:
            var1, var2 = variable[0], variable[-1]
            variables.add(var1)
            variables.add(var2)
 
        equal_var = {var : var for var in variables}
        rank = {var: 0 for var in variables}
        
        def find(var):
            if equal_var[var] == var:
                return var
            
            return find(equal_var[var])
        
        def union(var1, var2):
            equal1 = find(var1)
            equal2 = find(var2)

            if equal1 != equal2:

                if rank[equal1] > rank[equal2]:
                    equal_var[equal2] = equal1
                
                elif rank[equal2] > rank[equal1]:
                    equal_var[equal1] = equal2

                else:
                    equal_var[equal2] = equal1
                    rank[equal1] += 1
        
        result = True
        for equality in equations:
            if equality[1] == "=":
                var1, var2 = equality[0], equality[-1]
                union(var1, var2)
        
        
        for equality in equations:
            var1, var2 = equality[0], equality[-1]

            if equality[1] == "!" and find(var1) == find(var2):
                return False
        
        return True
        