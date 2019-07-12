class Solution:
    def __init__(self):
        self.problem_id = 'project_euler:1'

    def solution(self):
        total = 0
        for i in range(1, 1000):
            if i % 3 == 0 or i % 5 == 0:
                total += i

        return total
