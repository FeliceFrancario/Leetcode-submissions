class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        H={
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            '0':0
        }
        res=[0]*(len(num1)+len(num2))
        num1,num2=num1[::-1],num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j]+=H[num1[i]]*H[num2[j]]
                res[i+j+1]+=res[i+j]//10
                res[i+j]=res[i+j]%10
        res=res[::-1]
        start=0
        while start<len(res) and res[start]==0:
            start+=1
        
        
        res=map(str,res[start:])
        return "".join(res)

        