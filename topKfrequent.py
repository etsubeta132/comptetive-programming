class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}
        for item in nums:
            if item in dic:
                dic[item] += 1

            else:
                dic[item] = 1
        temp = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        key, value = zip(*temp)
        return list(key[:k])
