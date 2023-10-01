items = input("Enter the items, separating them with commas: ")
items_list = [item for item in items.split(', ')]
print(items_list)
if len(items_list) == 2:
    print("%s and %s" % (items_list[0], items_list[1]))
elif len(items_list) == 1:
    print(items_list[0])
else:
    items_list[-1] = " and " + items_list[-1]
    for l in items_list:
        l = ', '.join(items_list[0:-2]) + items_list[-1]
    print(l)