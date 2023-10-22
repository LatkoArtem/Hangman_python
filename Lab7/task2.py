def quadratic_equation(a, b, c):
    try:
        D = b**2 - 4*a*c    
        if D > 0: 
            x1 = round((-b + D**0.5)/(2*a), 3)
            x2 = round((-b - D**0.5)/(2*a), 3)
            return(x1, x2)
        elif D==0:
            x1 = round((-b)/(2*a), 3) 
            return(x1)
        else:
            raise ValueError('NO VALID ROOTS!')
    except ZeroDivisionError:
        raise ValueError("'a' cannot be 0 because then it would not be a quadratic equation")
            
while True:
    try:
        a = float(input("'a': "))
        break
    except ValueError:
        print("Variable 'a' must be a number")
while True:
    try:
        b = float(input("'b': "))
        break
    except ValueError:
        print("Variable 'b' must be a number")    
while True:
    try:
        c = float(input("'c': "))
        break
    except ValueError:
        print("Variable 'c' must be a number")
try:   
    res = quadratic_equation(a, b, c)
    if res:
        print(f'Result: {res}')
except ValueError as e:
    print(f'Result: {e}')