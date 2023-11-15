def countHomogenous(self, s: str) -> int:
        modulo = 10**9 + 7
        prev  = ''
        res = 0
        count = 0

        for i in s:
            if i == prev:
                count += 1
            else:
                count = 1
            
            res = (res + count) % modulo
            prev = i
            
        return res

