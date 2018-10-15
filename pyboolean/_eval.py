from _constants import operators

def eval_expr(expr):
    stack = []

    for i in expr:
        if i in operators:
            if i == '!' or i == '~' or i == '¬':
                x = stack.pop()
                x = int(not x)
                stack.append(x)
            else:
                x = stack.pop()
                y = stack.pop()
                z = int(operators[i](x, y))
                stack.append(z)
        else:
            stack.append(int(i))

    return stack[0]

def eval_func(func, inputs):
    func_replaced = ''
    operand_count = 0

    for i in func:
        if i in operators:
            func_replaced += i
        else:
            func_replaced += str(inputs[operand_count])
            operand_count += 1
    return eval_expr(func_replaced)
