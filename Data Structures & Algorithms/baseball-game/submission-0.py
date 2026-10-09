class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i, o in enumerate(operations):
            if o =="+":
                stack.append(int(stack[-1])+int(stack[-2]))
            elif o=="C":
                stack.pop()
            elif o=="D":
                stack.append(int(stack[-1])*2)
            else:
                stack.append(int(o))
        return sum(stack)

        