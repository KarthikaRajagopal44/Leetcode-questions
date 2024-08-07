# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in operators:
                right_operand = stack.pop()
                left_operand = stack.pop()
                if token == "+":
                    result = left_operand + right_operand
                elif token == "-":
                    result = left_operand - right_operand
                elif token == "*":
                    result = left_operand * right_operand
                else:
                    result = int(left_operand / right_operand)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]
    
    # https://leetcode.com/problems/evaluate-reverse-polish-notation/solutions/3206849/150-solution-with-step-by-step-explanation