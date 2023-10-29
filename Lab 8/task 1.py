import numpy as np
import itertools


def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (dim, dim))
    return matrix

def calculate_permutations(dim):
    """
    Calculate all permutations of length dim.
    """
    permutations = list(itertools.permutations(range(dim), dim))
    return permutations

def calculate_products(matrix, permutations):
    """
    Calculate the products of elements in the matrix 
    using the given permutations.
    """
    products = []
    for permutation in permutations:
        product = 1
        for i in range(len(permutation)):
            product *= matrix[i][permutation[i]]
        products.append(product)
    return products

def calculate_sign(permutations):
    """
    Calculate the sign of each permutation.
    """
    signs = []
    for perm in permutations:
        sign = 1
        for i in range(len(perm)):
            for j in range(i + 1, len(perm)):
                if perm[i] > perm[j]:
                    sign *= -1
        signs.append(sign)
    return signs 

def calculate_det(signs, products):
    """
    Calculate the determinant(detA) of a matrix.
    """
    determinant = sum(sign * product for sign, product in zip(signs, products))
    return determinant

while True:
    try:
        dim = int(input("Enter the dimension of the matrix: "))
        if dim <= 0:
            raise ValueError
        break
    except ValueError:
        print("The value of the dimension must be a whole positive integer")

matrix = random_matrix(dim)
print(f"A random matrix of the {dim} dimension:\n{matrix}")
print(f"detA = {calculate_det(calculate_sign(calculate_permutations(dim)), calculate_products(matrix, calculate_permutations(dim)))}")
print(f"Verification result of the calculation of the determinant: {np.linalg.det(matrix)}")