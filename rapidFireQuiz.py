import random
import ast

operations = ["%", "//", "+", "-", "*"]

def operationExpressionBuilder(length):
    if(length%2==0): length +=1
    i = 0
    expression = ""
    while(i<length):
        if(i%2==0): expression += str(random.randint(1, 11))
        else: expression += str(random.choice(operations))
        i+=1
    return expression

def getSolution(expression):
    return multiline_eval(expression)
    
def lstExpressionBuilder():
    expression = ""
    lst = list(range(random.randint(3, 11)))
    expression += "lst=" + str(lst) + "\n"
    index = random.randint(0, len(lst)-1)
    upTo = random.randint(index, len(lst))
    steps = random.randint(2, len(lst)//2)
    expression+= "lst[" + str(index) + ":" + str(upTo) + ":" + str(steps) + "]\n"
    try: 
        multiline_eval(expression)
        return expression
    except: 
        lstExpressionBuilder()

#From https://stackoverflow.com/questions/12698028/why-is-pythons-eval-rejecting-this-multiline-string-and-how-can-i-fix-it
def multiline_eval(expr):
    "Evaluate several lines of input, returning the result of the last line"
    tree = ast.parse(expr)
    eval_expr = ast.Expression(tree.body[-1].value)
    exec_expr = ast.Module(tree.body[:-1])
    exec(compile(exec_expr, 'file', 'exec'))
    return eval(compile(eval_expr, 'file', 'eval'))

        
                