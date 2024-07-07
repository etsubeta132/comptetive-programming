# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        i = 0
        while i < len(v1) and i < len(v2):
            if v1[i] == v2[i]:
                i += 1
            elif v1[i] > v2[i]:
                return 1
            else:
                return -1
        re = False
        if len(v2) > len(v1):
            v1, v2 = v2, v1
            re = True

        while i < len(v1):
            if v1[i] > 0:
                if re:
                    return -1
                return 1
            i += 1

        return 0