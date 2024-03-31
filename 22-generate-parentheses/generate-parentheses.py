class Solution:
    def check(self, sequence):
        stack = []
        for ch in sequence:
            if ch == '(':
                stack.append(ch)
            else:
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
        return True

    def recursion(self, curString, left, right, output):
        if left == 0 and right == 0:
            if curString[0] != ')' and curString[-1] != '(' and self.check(curString):
                output.append(curString)
        
        if left != 0:
            self.recursion(curString + '(', left - 1, right, output)
        if right != 0:
            self.recursion(curString + ')', left, right - 1, output)

    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.recursion('', n, n, output)
        return output