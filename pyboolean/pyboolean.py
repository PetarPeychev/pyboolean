# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org>

class BoolExpr:
    def __init__(self, expr):
        self._infix_expr = self._format(expr)
        self._postfix_expr = self._infix_to_postfix(self._infix_expr)
        self._infix_tokens = self._infix_expr.split()
        self._postfix_tokens = self._postfix_expr.split()
        self._infix_constants, self._infix_variables = self._consts_vars(self._infix_tokens)
        self._postfix_constants, self._postfix_variables = self._consts_vars(self._postfix_tokens)

    def __str__(self):
        return str(self._infix_expr)

    _OPERATOR_FUNCTIONS = {
        '.' : lambda x, y : str(int(int(x) and int(y))),
        '+' : lambda x, y : str(int(int(x) or int(y))),
        '!' : lambda x : str(int(not int(x)))
    }

    _OPERATOR_TOKENS = {
        'not' : ' ! ',
        '!' : ' ! ',
        '~' : ' ! ',
        '¬' : ' ! ',
        'and' : ' . ',
        '.' : ' . ',
        '&' : ' . ',
        '∧' : ' . ',
        'or' : ' + ',
        '+' : ' + ',
        '|' : ' + ',
        '∨' : ' + ',
        '(' : ' ( ',
        ')' : ' ) '
    }

    _OPERATOR_PRECEDENCE = {
        '!' : 3,
        '.' : 2,
        '+' : 1,
        '(' : 0
    }

    class _Stack:
        def __init__(self):
            self.elements = []

        def push(self, item):
            self.elements.append(item)

        def pop(self):
            return self.elements.pop()

        def peek(self):
            return self.elements[len(self.elements)-1]

        def isEmpty(self):
             return self.elements == []

        def len(self):
             return len(self.elements)

    def _format(self, expr):
        for token in self._OPERATOR_TOKENS.keys():
            if token in expr:
                expr = expr.replace(token, self._OPERATOR_TOKENS[token])
                expr = ' '.join(list(filter(None, expr.split())))
        return expr

    def _infix_to_postfix(self, expr):
        op_stack = self._Stack()
        postfix_list = []
        token_list = expr.split()

        for token in token_list:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" or token in "01":
                postfix_list.append(token)
            elif token == '(':
                op_stack.push(token)
            elif token == ')':
                top_token = op_stack.pop()
                while top_token != '(':
                    postfix_list.append(top_token)
                    top_token = op_stack.pop()
            else:
                while (not op_stack.isEmpty()) and (self._OPERATOR_PRECEDENCE[op_stack.peek()] >= self._OPERATOR_PRECEDENCE[token]):
                    postfix_list.append(op_stack.pop())
                op_stack.push(token)

        while not op_stack.isEmpty():
            postfix_list.append(op_stack.pop())
        return " ".join(postfix_list)

    def _consts_vars(self, expr_tokens):
        consts = []
        vars = []
        for token in expr_tokens:
            if token in self._OPERATOR_FUNCTIONS or token in '()':
                pass
            elif token in '01':
                consts.append(token)
            elif token in vars:
                pass
            else:
                vars.append(token)
        return consts, vars

    def eval(self, *args):
        if len(args) != len(self._infix_variables):
            raise TypeError('incorrect number of arguments to replace variables in expression')
        tokens = self._postfix_tokens
        assigned_vars = {}
        for token in tokens:
            if token in self._postfix_variables:
                if token not in assigned_vars:
                    assigned_vars[token] = str(int(args[0]))
                tokens = [assigned_vars[token] if (x == token) else x for x in tokens]

        stack = self._Stack()
        for token in tokens:
            if token in self._OPERATOR_FUNCTIONS:
                if token == '!':
                    x = stack.pop()
                    x = self._OPERATOR_FUNCTIONS[token](x)
                    stack.push(x)
                else:
                    x = stack.pop()
                    y = stack.pop()
                    z = self._OPERATOR_FUNCTIONS[token](x, y)
                    stack.push(z)
            else:
                stack.push(token)
        return stack.peek()

    def truthdict(self):
        dict = {}
        vars_num = len(self._infix_variables)
        for i in range(2 ** vars_num):
            args = tuple(format(i, 'b').zfill(vars_num))
            output = self.eval(*args)
            dict[args] = output
        return dict

    def truthtable(self):
        dict = self.truthdict()
        table = '╔' + '═══' * len(self._infix_variables) + '══════╗\n'
        table += '║  '
        for var in self._infix_variables:
            table += var + '  '
        table += '┃ O ║\n'
        table += '║━━'
        table += '━━━' * len(self._infix_variables) + '╋━━━║'
        for row in dict:
            table += '\n'
            table += '║  '
            for input in row:
                table += input + '  '
            table += '┃ ' + dict[row] + ' ║'
            if row == list(dict.keys())[-1]:
                table += '\n╚' + '═══' * len(self._infix_variables) + '══════╝'
            else:
                table += '\n' + '║──' + '───' * len(self._infix_variables) + '╂───║'
        return table
