class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        path=[]
        res=[]
        l=len(candidates)
        candidates.sort()
        def dfs(i,path_sum):
            if path_sum==target:
                res.append(path.copy())
                return
            if path_sum>target:
                return
            for j in range(i,l):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                path.append(candidates[j])
                dfs(j+1,path_sum + candidates[j])
                path.pop()
        dfs(0,0)
        return res


        