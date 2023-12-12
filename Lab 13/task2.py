def fib(n):
    fib_list = [1, 1]
    while len(fib_list) < n: 
        fib_list.append(fib_list[-1] + fib_list[-2])
    for num in fib_list:
        yield num

while True:        
    try:
        n = int(input('Enter N: '))
        if n >= 1:
            break
        else:
            print("Enter a positive integer") 
    except ValueError:
        print("Enter a positive integer")   
        
for index, number in enumerate(fib(n)):
    print(number, end=', ' if index < n - 1 else '')