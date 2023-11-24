def root2(i):
    if i >= 0:
        result = i**(1/2)
        if result % 1 == 0:
            return int(result)
        else:
            return round(result, 5)
    
def root3(i):
    if i < 0:
        result = abs(i)**(1/3)
        if result % 1 == 0:
            result = int(result)
            output = f"-{result}"
            return output
        else:
            output = f"-{result}"
            return output
    else:
        result = i**(1/3)
        if result % 1 == 0:
            return int(result)
        else:
            return result