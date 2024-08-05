# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}
        preq_count = {i:0 for i in range(numCourses)}
    
        for course, pre in prerequisites:
            preq[pre].append(course)
            preq_count[course] += 1
    


        stack = []
        for cour, ctr in  preq_count.items():
            if ctr == 0:
                stack.append(cour)
        
        courses = []
        while stack:
            course = stack.pop()
            courses.append(course)
            for pre in preq[course]:
                preq_count[pre] -= 1

                if preq_count[pre] == 0:
                    stack.append(pre)
        
        if len(courses) == numCourses:
            return True
        else:
            return False
        
        


        