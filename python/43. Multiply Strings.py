class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        # reverse traversal (like manual multiplication)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]
                
                res[p2] = total % 10
                res[p1] += total // 10
        
        # convert to string, skip leading zeros
        result = []
        for num in res:
            if not (len(result) == 0 and num == 0):
                result.append(str(num))
        
        return ''.join(result) if result else "0"