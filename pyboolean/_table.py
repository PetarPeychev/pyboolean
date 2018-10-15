from _constants import operators
from _eval import eval_func
import itertools
import pprint
from tabulate import tabulate

def _params_list(func):
    params = []

    for i in func:
        if i not in operators:
            params.append(i)

    return params

def _inputs(param_count):
    inputs = []
    row = 0

    for i in itertools.product([0, 1], repeat=param_count):
        inputs.append([])
        column = 0

        for j in i:
            inputs[row].append(j)
            column += 1
        row += 1

    return inputs

def truthtable(func):
    params = _params_list(func)
    inputs_list = _inputs(len(params))
    truthtable = []

    for inputs in inputs_list:
        output = eval_func(func, inputs)
        truthtable.append((inputs, output))

    return truthtable

def format(truthtable):
    param_count = len(truthtable[0][0])
    table = '╔' + '═══' * param_count + '══════╗\n'
    table += '║  '

    for i in range(param_count):
        table += chr(i + 65) + '  '

    table += '┃ O ║\n'
    table += '║━━'
    table += '━━━' * param_count + '╋━━━║'

    for row in truthtable:
        table += '\n'
        table += '║  '
        for param in row[0]:
            table += str(param) + '  '
        table += '┃ ' + str(row[1]) + ' ║'
        if row == truthtable[len(truthtable) - 1]:
            table += '\n╚' + '═══' * param_count + '══════╝'
        else:
            table += '\n' + '║──' + '───' * param_count + '╂───║'

    return table
