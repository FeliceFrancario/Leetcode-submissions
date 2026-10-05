class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+','-','*','/']
        stack=[]
        for c in tokens:
            if c in operators:
                a=stack.pop()
                b=stack.pop()
                if c=='+':
                    stack.append(int(b)+int(a))
                elif c=='-':
                    stack.append(int(b)-int(a))
                elif c=='*':
                    stack.append(int(b)*int(a))
                elif c=='/':
                    stack.append(int(b/a))
            else:
                stack.append(int(c))

        return stack[0]
            