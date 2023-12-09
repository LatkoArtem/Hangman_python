def fib(n):
    fib_list = [0, 1]
    while len(fib_list) < n+1: 
        fib_list.append(fib_list[-1] + fib_list[-2])
    result = ', '.join(map(str, fib_list))
    return result

while True:        
    try:
        n = int(input('Enter N: '))
        if n >= 1:
            break
        else:
            print("Enter a positive integer") 
    except ValueError:
        print("Enter a positive integer")   
        
print(fib(n))