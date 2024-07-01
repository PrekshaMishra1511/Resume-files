'''class SimpleCalculator:
    def __init__(self):
        self.history = []

    def evaluate_expression(self, expression):
        expression = expression.replace(" ", "")

        if len(expression) != 3:
            result = "Error"
            self.history.insert(0, (expression, result))
            return result

        first_operand = int(expression[0])
        operator = expression[1]
        second_operand = int(expression[2])

        try:
            if operator == '+':
                result = float(first_operand + second_operand)
            elif operator == '-':
                result = float(first_operand - second_operand)
            elif operator == '*':
                result = float(first_operand * second_operand)
            elif operator == '/':
                if second_operand == 0:
                    result = "Error"
                else:
                    result = float(first_operand / second_operand)
            else:
                result = "Error"
        except:
            result='Error'

        self.history.insert(0, (expression, result))
        return result

    def get_history(self):
        return self.history'''


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if len(self.stack) == 0:
            return 'Error'
        else:
            return self.stack[-1]

    def pop(self):
        if len(self.stack) == 0:
            return 'Error'
        else:
            return self.stack.pop()

    def is_empty(self):
        return self.stack == []

    def __str__(self):
        return ' '.join(str(item) for item in self.stack)

    def __len__(self):
        return len(self.stack)


class AdvancedCalculator():
    def __init__(self):
        self.history = []
        self.operator_stack = Stack()
        self.operand_stack = Stack()

    def evaluate_expression(self, expression):
        print(expression)
        #super().evaluate_expression(expression)
        tokens = self.tokenize(expression)
        if not self.check_brackets(tokens):
            return "Error"
        result = self.evaluate_list_tokens(tokens)
        self.history.insert(0, (expression, result))
        return result

    def tokenize(self, expression):
        print('tokenize',expression)
        tokens = []
        current_token = ""
        for char in expression:
            if char.isdigit():
                current_token += char
            elif char in ['+', '-', '*', '/', '(', ')', '{', '}']:
                if current_token:
                    tokens.append(int(current_token))
                    current_token = ""
                tokens.append(char)
        if current_token:
            tokens.append(int(current_token))
        return tokens

    def check_brackets(self, token_list):
        print('check',token_list)
        bracket_stack = Stack()
        for token in token_list:
            if token in ['(', '{']:
                bracket_stack.push(token)
            elif token in [')', '}']:
                if bracket_stack.is_empty():
                    return False
                opening_bracket = bracket_stack.pop()
                if (token == ')' and opening_bracket != '(') or (token == '}' and opening_bracket != '{'):
                    return False
        return bracket_stack.is_empty()

    def evaluate_list_tokens(self, token_list):
        print('evaluate',token_list)
        for token in token_list:
            if isinstance(token, int):
                self.operand_stack.push(token)
            elif token in ['+', '-', '*', '/']:
                while not self.operator_stack.is_empty() and self.operator_stack.peek() != '(' and \
                        self.precedence(token) <= self.precedence(self.operator_stack.peek()):
                    self.evaluate_top_operator()
                self.operator_stack.push(token)
            elif token in ['(', '{']:
                self.operator_stack.push(token)
            elif token in [')', '}']:
                while not self.operator_stack.is_empty() and self.operator_stack.peek() != '(' and \
                        self.operator_stack.peek() != '{':
                    self.evaluate_top_operator()
                self.operator_stack.pop()
        while not self.operator_stack.is_empty():
            if self.evaluate_top_operator() == 'Error':
                return 'Error'
        if self.operand_stack.is_empty():
            return "Error"
        return self.operand_stack.pop()

    def evaluate_top_operator(self):
        operator = self.operator_stack.pop()
        second_operand = self.operand_stack.pop()
        first_operand = self.operand_stack.pop()
        if second_operand == 'Error' or first_operand == 'Error':
            return 'Error'
        if operator == '+':
            self.operand_stack.push(float(first_operand + second_operand))
        elif operator == '-':
            self.operand_stack.push(float(first_operand - second_operand))
        elif operator == '*':
            self.operand_stack.push(float(first_operand * second_operand))
        elif operator == '/':
            self.operand_stack.push(float(first_operand / second_operand))

    @staticmethod
    def precedence(operator):
        if operator in ['+', '-']:
            return 1
        elif operator in ['*', '/']:
            return 2
        else:
            return 0

    def get_history(self):
        return self.history


calculator = AdvancedCalculator()
answer1 = calculator.evaluate_expression("2 + (3 / 4)")  # answer should be 2.75
answer2 = calculator.evaluate_expression("2 +")  # answer should be "Error"
tokens = calculator.tokenize("2 + 3")  # tokens should be [2, '+', 3]
answer3 = calculator.evaluate_list_tokens([2, '+', 3])  # answer should be 5.0
correct_brackets = calculator.check_brackets(['(', 2, '*'])  # should be False
history = calculator.get_history()  # history should be [("2 +", "Error"), ("2 + (3 /4)", 2.75)]
'''
print(answer1)
print(answer2)
print(tokens)
print(answer3)
print(correct_brackets)
print(history)
'''
