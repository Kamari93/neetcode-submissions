class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency_graph = [[] for _ in range(numCourses)]
        needed_courses = [0] * numCourses

        for a, b in prerequisites:
            dependency_graph[b].append(a)
            needed_courses[a] += 1
        
        q = [idx for idx, num in enumerate(needed_courses) if num == 0]

        for i in q:
            numCourses -= 1
            for j in dependency_graph[i]:
                needed_courses[j] -= 1
                if needed_courses[j] == 0:
                    q.append(j)
        
        return numCourses == 0