operators = {
    '&' : lambda x, y : x and y,
    '.' : lambda x, y : x and y,
    '∧' : lambda x, y : x and y,
    '+' : lambda x, y : x or y,
    '|' : lambda x, y : x or y,
    '∨' : lambda x, y : x or y,
    '!' : lambda x : not x,
    '~' : lambda x : not x,
    '¬' : lambda x : not x,
    '^' : lambda x, y : x ^ y,
    '⊕' : lambda x, y : x ^ y,
    '⊻' : lambda x, y : x ^ y
}

def eval(expr):
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
