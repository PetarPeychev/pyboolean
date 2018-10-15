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

operator_precedence = {
    '!' : 3,
    '~' : 3,
    '¬' : 3,
    '&' : 2,
    '.' : 2,
    '∧' : 2,
    '^' : 1,
    '⊕' : 1,
    '⊻' : 1,
    '+' : 0,
    '|' : 0,
    '∨' : 0
}
