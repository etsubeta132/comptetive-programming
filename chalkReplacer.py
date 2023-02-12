class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        sums=sum(chalk)
        k=k%sums
        i=0

        while(k>=0):
            if i < len(chalk):
                k-=chalk[i]
                i+=1
            
        return i-1
