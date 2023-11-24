tree = [2, [7, [2, [], []], [6, [5, [], []], [11, [], []]]], [5, [], [9, [4, [], []], []]]]

def tree_travaling(tree):
    if tree:
        if tree[2]:
            right_subtree = tree_travaling(tree[2])
            for value_r in right_subtree:
                yield value_r
        yield tree[0]
        if tree[1]:
            left_subtree = tree_travaling(tree[1])
            for value_l in left_subtree:
                yield value_l

output = tree_travaling(tree)
print(" ".join(str(value) for value in output))
