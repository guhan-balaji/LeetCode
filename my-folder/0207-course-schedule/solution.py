class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0] * numCourses
        graph = {i: [] for i in range(numCourses)}
        q = deque([])

        for [course, pre] in prerequisites:
            in_degrees[course] += 1
            graph[pre].append(course)

        for course, in_degree in enumerate(in_degrees):
            if in_degree == 0:
                q.append(course)
        
        while q:
            pre = q.popleft()

            for course in graph[pre]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0 : q.append(course)
        
        return sum(in_degrees) == 0
