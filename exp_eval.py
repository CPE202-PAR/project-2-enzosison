from stack_array import Stack

# You should not change this Exception class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""

    operandStack = Stack(30)
    tokenList = input_str.split()
    s = ('+', '-', '*', '**', '>>', '<<', '/')

    for item in tokenList:
        try:
            x = float(item)
        except ValueError:
            x = None
            if x is None and item not in s: #value must be a letter or another invalid token
                raise PostfixFormatException("Invalid token")
    count = 0 #we need a count to keep track of the total number of operands in our string
    for item in tokenList:
        try:
            x = float(item)
        except ValueError:
            x = None
            if x is not None: #this is a valid operand
                count +=1
            elif x in s:
                count -= 1 #not focusing on operators -> looking for operands
            if count < 1:
                raise PostfixFormatException("Insufficient operands")


    for token in tokenList:
        if token not in s:
            val = convert_num(token) #int / float conversion for operands
            operandStack.push(val)
        elif token in s:
            num_1 = operandStack.pop()
            num_2 = operandStack.pop()
            new_num = do_math(num_1, num_2, token)
            operandStack.push(new_num)
    if operandStack.num_items != 1:
        raise PostfixFormatException("Too many operands")
    final = operandStack.pop()
    return final

def convert_num(num):
    if "." in num:
        return float(num)
    else:
        return int(num)

def do_math(num_1, num_2, token):
    if token == "<<":
        return num_1 << num_2
    elif token == ">>":
        return num_1 >> num_2
    elif token == "*":
        return num_1 * num_2
    elif token == "/":
        return num_1 / num_2
    elif token == "+":
        return num_1 + num_2
    elif token == "-":
        return num_1 - num_2
    else:
        return num_1**num_2

def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    prec = {} #hold precedence values for operators
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack(30)
    postfixList = []
    tokenList = input_str.split()

    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        if token == "(":
            opStack.push(token)
        if token == ")":
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()

    #perform for operator uaing precedence

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    opStack = Stack(30)
    s = ('+', '-', '*', '**', '>>', '<<', '/')
    tokenList = input_str.split()

    for i in reversed(tokenList):
        if i in "0123456789":
            opStack.push(i)
        if i in s:
            op1 = opStack.pop()
            op2 = opStack.pop()
            string = op1 + op2 + i
            opStack.push(string)
        final = opStack.pop()
        return(final)




