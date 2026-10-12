class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses={i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courses[course].append(prereq)
        visited=set()
        cycle=set()
        res=[]
        def dfs(course):
            
            if course in cycle:
                return False
            if course in visited:
                return True
            visited.add(course)
            cycle.add(course)

            for p in courses[course]:
                if not dfs(p):
                    return False
            cycle.remove(course)
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return list(res)
            