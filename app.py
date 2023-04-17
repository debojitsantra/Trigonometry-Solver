import math

# Define a list of allowed functions
allowed_functions = ["sin", "cos", "tan", "cot", "sec", "csc"]

# Define a function to evaluate a single term
def eval_term(term):
    # Find the function and argument in the term
    for func in allowed_functions:
        if func in term:
            func_start = term.find(func)
            arg_start = func_start + len(func)
            arg_end = len(term) - 1 if term[-1] != ")" else term.rfind(")") + 1
            arg = term[arg_start:arg_end]
            break
    else:
        # If no function found, assume it's a number
        return float(term)

    # Evaluate the function
    arg = eval_expr(arg)
    if func == "sin":
        return math.sin(math.radians(arg)) ** 2
    elif func == "cos":
        return math.cos(math.radians(arg)) ** 2
    elif func == "tan":
        return math.tan(math.radians(arg)) ** 2
    elif func == "cot":
        return 1 / math.tan(math.radians(arg)) ** 2
    elif func == "sec":
        return 1 / math.cos(math.radians(arg)) ** 2
    elif func == "csc":
        return 1 / math.sin(math.radians(arg)) ** 2

# Define a function to evaluate an expression
def eval_expr(expr):
    # Split the expression into terms
    terms = []
    term_start = 0
    for i in range(len(expr)):
        if expr[i] in "+-*/":
            terms.append(expr[term_start:i])
            term_start = i
    terms.append(expr[term_start:])

    # Evaluate each term and combine the results
    result = eval_term(terms[0])
    for i in range(1, len(terms)):
        term = eval_term(terms[i])
        if expr[i-1] == "+":
            result += term
        elif expr[i-1] == "-":
            result -= term
        elif expr[i-1] == "*":
            result *= term
        elif expr[i-1] == "/":
            result /= term

    return result

# Prompt the user to enter an expression
expression = input("Enter a trigonometry expression: ")

# Evaluate the expression
result = eval_expr(expression)

# Print the result
print(f"The result is {result:.2f}")
