# from collections import defaultdict, deque
# n = int(input())

# preq = defaultdict(list)
# indegree = defaultdict(int)

# for  i in range(n - 1):
#     nums = list(map(int, input().split()))
#     preq[nums[0]].append(nums[1])
#     indegree[nums[1]] += 1
#     indegree[nums[0]] += 0


# queue = deque()
# for key, val in indegree.items():
#     if val == 0:
#         queue.append(key)


# preq = defaultdict(set)
# while queue:
#     num = queue.popleft()

#     for child in preq[num]:
#         preq[child].add(num)
#         preq[child].update(preq[num])

#         indegree[child] -=1

#         if indegree[child] == 0:
#             queue.append(child)

# print(*order[::-1])

# def smmm(n, words):
#     prefix = [0] * 26

#     tot_ln = 0

#     for word in words:
#         for char in word:
#             idx = ord(char) - ord("a")
#             prefix[idx] += 1
#         tot_ln += len(word)

#     sm = 0

#     for word in words:
#         for char in word:
#             idx = ord(char) - ord("a")
#             sm += tot_ln - prefix[idx]
#     return sm

# n = int(input())

# words = []
# for _ in range(n):
#     word = input()
#     words.append(word)
# print(smmm(n, words))

class Node:
    def __init__(self):
        self.is_end = False
        self.children  = {}
    
class Trie:
    def __init__(self):
        self.trie = Node()
    
    def insert(self, word):
        cur = self.trie

        for w in word:

            if w not in cur.children:
                cur.children[w] = Node()
            
            cur = cur.children[w]
    
    def xorSum(l, r):
        
    
        
    
 
# n = int(input())
# length = list(map(int, input().split()))

# words = []
# prefix = {}

# for ln in length:
#     if ln == 1:
#         words.append("0")
#         prefix["0"] = 1
#     else:

    
    
