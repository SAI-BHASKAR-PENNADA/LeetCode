class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = self.stack.pop()
                a = self.stack.pop()
                if token == '+':
                    self.stack.append(a + b)
                elif token == '-':
                    self.stack.append(a - b)
                elif token == '*':
                    self.stack.append(a * b)
                else:
                    ans = a / b
                    self.stack.append(int(ans))
                    # if ans < 0:
                    #     self.stack.append(math.ceil(ans))
                    # else:
                    #     self.stack.append(math.floor(ans))
                # print(a,b,self.stack[-1])
            else:
                self.stack.append(int(token))
        
        return self.stack.pop()