class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Stack to hold characters and intermediate boolean values
        stack = []
        
        for char in expression:
            if char == ')':
                # When we find a closing parenthesis, we need to evaluate the sub-expression
                sub_expr = []
                
                # Pop all elements until we find the opening parenthesis
                while stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop()  # Remove '('
                
                # The operator just before the '('
                operator = stack.pop()
                
                # Now evaluate based on the operator
                if operator == '&':
                    # AND operation: all elements in sub_expr must be 't' (True)
                    result = all(x == 't' for x in sub_expr)
                elif operator == '|':
                    # OR operation: at least one element in sub_expr must be 't' (True)
                    result = any(x == 't' for x in sub_expr)
                elif operator == '!':
                    # NOT operation: exactly one element to negate
                    result = sub_expr[0] == 'f'
                
                # Push the result back to the stack as 't' or 'f'
                stack.append('t' if result else 'f')
                
            elif char != ',':
                # Push every character that is not a comma to the stack
                stack.append(char)
        
        # The final result will be the last element in the stack
        return stack.pop() == 't'
