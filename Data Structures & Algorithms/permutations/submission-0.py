class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]

        def dfs(path):
            if len(path)==len(nums):
                res.append(path.copy())
                return 
            for n in nums:
                if n in path:
                    continue
                path.append(n)
                dfs(path)
                path.pop()
            return res
        return dfs([])

        