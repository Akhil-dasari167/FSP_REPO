# Converting nested tuple to nested list

def converttup(x):
    if isinstance(x, tuple):
        return [converttup(i) for i in x]
    return x


# Converting nested list to nested tuple

def convertlst(x):
    if isinstance(x, list):
        return tuple(convertlst(i) for i in x)
    return x


# Nested List
my_list = [[[1, 2], [13, 4]], [[5, 6], [7, 8]]]

b = convertlst(my_list)

print("List to Tuple:")
print(b)


# Another List
lst = [1, 2, 3, 4, [5, 6, 7]]

c = convertlst(lst)

print("\nAnother List to Tuple:")
print(c)


# Nested Tuple
a = ((1, 2), (3, 4), ((5, 6), (7, 8)))

d = converttup(a)

print("\nTuple to List:")
print(d)