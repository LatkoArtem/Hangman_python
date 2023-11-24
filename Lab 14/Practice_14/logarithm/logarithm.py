import math

def log(a, b):
    if a>0 and a!=1:
        if b>0:
            return math.log(b, a)
    else:
        raise ValueError
    
def ln(b):
    if b>0:
        return math.log(b)
    
def lg(b):
    if b>0:
        return math.log10(b)
    