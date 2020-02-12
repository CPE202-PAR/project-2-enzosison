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

    bigStack = Stack(30)
    list_tokens = input_str.split()
    s = ('+', '-', '*', '**', '>>', '<<', '/')

    for item in list_tokens:
        try:
            x = float(item)
        except ValueError:
            if item not in s: #value must be a letter or another invalid token
                raise PostfixFormatException("Invalid token")

    if len(list_tokens) == 0:
        raise PostfixFormatException("Insufficient operands")

    for token in list_tokens:
        if token not in s:
            val = convert_num(token) #int / float conversion for operands
            bigStack.push(val)

        elif token in s:

            if bigStack.num_items < 2:
                raise PostfixFormatException("Insufficient operands")

            num_1 = bigStack.pop()
            num_2 = bigStack.pop()
            new_num = do_math(num_1, num_2, token)
            bigStack.push(new_num)

    if bigStack.num_items > 1:
        raise PostfixFormatException("Too many operands")

    final = bigStack.pop()
    return final

def convert_num(num):
    if "." in num:
        return float(num)
    else:
        return int(num)

def do_math(num_1, num_2, token):
    if token == "<<":
        return num_1 * (2**num_2)
    elif token == ">>":
        return num_1 / (2**num_2)
    elif token == "*":
        return num_1 * num_2
    elif token == "/":
        return num_1 / num_2
    elif token == "+":
        return num_1 + num_2
    elif token == "-":
        return num_1 - num_2
    else:
        return num_2**num_1

def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    prec = {} #hold precedence values for operators
    prec["<<"] = [5, "Left"]
    prec[">>"] = [5, "Left"]
    prec["**"] = [4, "Right"]
    prec["*"] = [3, "Left"]
    prec["/"] = [3, "Left"]
    prec["+"] = [2, "Left"]
    prec["-"] = [2, "Left"]
    prec["("] = [1, "Left"]
    prec[")"] = [1, "Left"]
    bigStack = Stack(30)
    finalList = []
    tokens = input_str.split()

    for token in tokens:
        if token not in prec:
            finalList.append(token)
            # bigStack.push(token)
            continue

        elif token == "(":
            bigStack.push(token)
            continue

        elif token == ")":
            topToken = bigStack.pop()
            while topToken != '(':
                finalList.append(topToken)
                topToken = bigStack.pop()
            continue

        elif token == "**" and (not bigStack.is_empty()) and bigStack.peek() == "**":
            bigStack.push(token)

    #perform for operator using precedence
        elif token in prec:
            while (not bigStack.is_empty()) and bigStack.peek() in prec and ((prec[token][1] == "Left" and prec[bigStack.peek()][0] >= prec[token][0]) or \
                    (prec[token][1] == "Right" and prec[bigStack.peek()][0] > prec[token][0])):
                # if (prec[token][1] == "Left" and prec[bigStack.peek()][0] >= prec[token][0]) or \
                #     (prec[token][1] == "Right" and prec[bigStack.peek()][0] > prec[token][0]):
                        topToken = bigStack.pop()
                        finalList.append(topToken)
            bigStack.push(token)

        else:
            finalList.append(token)
    while not bigStack.is_empty():
        finalList.append(bigStack.pop())
    return " ".join(finalList)


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    bigStack = Stack(30)
    s = ('+', '-', '*', '**', '>>', '<<', '/')
    list_tokens = input_str.split()

    for i in reversed(list_tokens):
        if i not in s:
            bigStack.push(i)
        else:
            op1 = bigStack.pop()
            op2 = bigStack.pop()
            string = op1 + " " + op2 + " " + i
            bigStack.push(string)
    final = bigStack.pop()
    return(final)




