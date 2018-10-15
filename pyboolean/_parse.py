from _constants import operators, operator_precedence

def infix_to_rpn(expr):
    output_stack = []
    operator_stack = []

    for token in expr:
        if token not in operators:
            output_stack.append(token)
        else:
            pass
            # TODO: Implement shunting-yard
