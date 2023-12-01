class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total = sum(salary[1:-1])
        lg = len(salary)-2
        avg = total/lg
        print(salary[0],salary[len(salary)-1])
        return avg