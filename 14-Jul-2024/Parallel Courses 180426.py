# Problem: Parallel Courses - https://www.codingninjas.com/codestudio/problems/parallel-courses_1376444

from collections import deque

def parallelCourses(n, prerequisites):
    
    indegree = {i:0 for i in range(1, n + 1)}
    prerequisit = {i:[] for i in range(1, n + 1)}
    
    
    for preq, course in prerequisites:
        prerequisit[preq].append(course)
        indegree[course] +=  1
    
    semister_count = 0
    visited = set()
    queue = deque()
    
    for key, val in indegree.items():
        if val == 0:
            queue.append(key)
            visited.add(key)
    
    while queue:
        ln = len(queue)
        
        semister_count += 1
        
        for i in range(ln):
            preq = queue.popleft()

            for course in prerequisit[preq]:
                indegree[course] -= 1

                if indegree[course] == 0 and course not in visited:
                    queue.append(course)
                    visited.add(course)
        
    
   
    if len(visited) == n:
        return semister_count
    else:
        return -1