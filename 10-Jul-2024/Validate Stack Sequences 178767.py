# Problem: Validate Stack Sequences - https://leetcode.com/problems/validate-stack-sequences/

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        index_1, index_2 =-1, 0
        stackV = []
        while index_2 < len(popped):
            if index_1 < len(pushed)-1:
                if not stackV:
                    stackV.append(pushed[index_1+1])
                    index_1 += 1
                else:
                    if stackV[-1] != popped[index_2]:
                        stackV.append(pushed[index_1+1])
                        index_1 += 1
            if stackV[-1] == popped[index_2]:
                stackV.remove(stackV[-1])
                index_2 += 1
            elif stackV[-1] != popped[index_2] and index_1 >= len(pushed)-1:
                return False

        if not stackV:
            return True
        else:
            return False
        