import random

operations = ["%", "//", "+", "-", "*"]

def expressionBuilder(length):
    if(length%2==0): length +=1
    i = 0
    expression = ""
    while(i<length):
        if(i%2==0): expression += str(random.randint(1, 11))
        else: expression += str(random.choice(operations))
        i+=1
    return expression

def getSolution(expression):
    return eval(expression)

        
                