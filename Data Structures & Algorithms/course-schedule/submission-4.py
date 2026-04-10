class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Adjacency Matrix
        # hashmap

        seen = set()
        
        preMap = defaultdict(list)
            # 0 : [1,2]
            # 1: [2]
            # 2: []
    
        for pre in prerequisites: #[0,1]
            preMap[pre[0]].append(pre[1])
        
        def dfs(course):
            
            # Prevent cycle
            if course in seen:
                return False 

            # Base case
            if preMap[course] == []:
                return True
            
            seen.add(course)

            for c in preMap[course]:
                if not dfs(c):
                    return False

            seen.remove(course)
            preMap[course] = [] # 0 : []

            return True 
        

        for course in range(numCourses):
            if not dfs(course): # dfs returns false, we dont want return true, not cancels it
                return False

        
        return True 
