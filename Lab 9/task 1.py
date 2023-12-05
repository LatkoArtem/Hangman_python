from functools import reduce

data = {
    -1: 154,
    5: -4152,
    0: "Hello!",
    54: 0.543243,
    2: "It's me!",
    "Why not?": 34
}

def is_num(value):
    return isinstance(value, (int, float))

def is_sum_key_and_values(i):
    return i[0] + i[1]

def is_positive_num(value):
    return value > 0

number1 = dict(filter(lambda i: is_num(i[0]) and is_num(i[1]), data.items()))
print(f"1.  {number1}")

number2 = list(map(lambda i: is_sum_key_and_values(i), number1.items()))
print(f"2.  {number2}")

number3 = reduce(lambda x, y: x + (is_positive_num(y) > 0), number2, 0)
print(f"3.  {number3}")