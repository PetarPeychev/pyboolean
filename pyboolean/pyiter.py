import pyeval
import itertools

def generate_operand_list(expr):
    operand_list = []

    for i in expr:
        if i not in pyeval.operators:
            operand_list.append(i)

    return operand_list

def generate_input_list(operand_count):
    input_list = []
    row = 0

    for i in itertools.product([0, 1], repeat=operand_count):
        input_list.append([])
        column = 0

        for j in i:
            input_list[row].append(j)
            column += 1
        row += 1

    return input_list

def eval_expr_with_inputs(expr, input_list):
    output_list = []
    for i in input_list:
        expr_replaced = ''
        operand_count = 0
        for j in expr:
            if j in pyeval.operators:
                expr_replaced += j
            else:
                expr_replaced += str(i[operand_count])
                operand_count += 1
        output_list.append(pyeval.eval(expr_replaced))
    return output_list



print(eval_expr_with_inputs('ab&', generate_input_list(len(generate_operand_list('ab&')))))
