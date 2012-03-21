import string
import tokens

from operators import Operator


class Expression:
    def __init__(self, expression):
        self.expression = expression.replace(' ', '').lower() + tokens.END
        print self.expression

    def solve(self, context):
        self.operands = []
        self.operators = []
        self.token = self.expression[0]
        self.position = 0
        self.error = None

        self.operators.append(Operator(tokens.SEN))
        self._parse_binary()
        self._expect_token(tokens.END)

        if not self.error:
            return self.operands[0]
        else:
            return self.error

    def _parse_binary(self):
        self._parse_primary()

        while self.token in tokens.BINARY_OPS and not self.error:
            self._push_operator(Operator(self.token))
            self._next_token()
            self._parse_primary()

        print self.operators
        print self.operands

        while self.operators[-1].symbol != tokens.SEN and not self.error:
            self._pop_operator()

    def _parse_primary(self):
        if self.token in string.digits:
            self._parse_digit()
        elif self.token == '-':
            self.operators.append(Operator(tokens.UNA_MIN))
            self._next_token()
            self._parse_primary()
        else:
            self.error = 'Error: Syntax error'

    def _parse_digit(self):
        parsed_number = ''

        while self.token in string.digits or self.token == '.':
            parsed_number += self.token
            self._next_token()

        self.operands.append(float(parsed_number))

    def _push_operator(self, op):
        precedence = tokens.get_precedence(op.symbol)

        while tokens.get_precedence(self.operators[-1].symbol) >= precedence:
            self._pop_operator()

        self.operators.append(op)

    def _pop_operator(self):
        symbol = self.operators[-1].symbol

        if symbol in tokens.UNARY_OPS + tokens.RIGHT_OPS:
            operator = self.operators.pop()
            operand = self.operands.pop()

            self.operands.append(operator.solve_unary(operand))
        elif symbol in tokens.BINARY_OPS:
            operator = self.operators.pop()
            operand1 = self.operands.pop()
            operand2 = self.operands.pop()

            self.operands.append(operator.solve_binary(operand2, operand1))

    def _next_token(self):
        if self.token != tokens.SEP and self.token != tokens.END:
            self.position += 1
            self.token = self.expression[self.position]

    def _expect_token(self, token):
        if self.token == token:
            self._next_token()
        else:
            self.error = "Error: Expected \'%s\', got \'%s\'" % \
            (token, self.token)
