def exp2(i):
    result = i**2
    if result % 1 == 0:
        return int(result)
    else:
        return round(result, 5)
    
def exp3(i):
    result = i**3
    if result % 1 == 0:
        return int(result)
    else:
        return round(result, 5)