def calculate(num1: float, num2: float, operator: str) -> float:
    num1 = float(input('num 1: '))
    num2 = float(input('num 2: '))
    
    operator = input('operator(+, -, *, /): ')
    if operator == '^':
        return 'bunday operator mavjud emas'
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return 'nomga bolish mumkin emas'
   

print(calculate(1, 2, '/'))

    
            
