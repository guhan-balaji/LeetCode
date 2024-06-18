class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a =  '0' * (len(b) - len(a)) + a
        elif len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        

        out = []
        z = 0
        for i in range(len(a) - 1, -1, -1):
            x = int(a[i])
            y = int(b[i])
            print(x, y)
            s = x + y + z
            if s < 2:
                out.append(str(s))
                z = 0
            elif s == 2:
                out.append('0')
                z = 1
            else:
                out.append('1')
                z = 1
        
        if z == 1:
            out.append('1')

        
        return ''.join(out[::-1])
