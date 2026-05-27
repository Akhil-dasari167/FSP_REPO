a = [1, (2,3), [4,5], (6,(7,8))]

list_count = 0
tuple_count = 0

def count_types(x):

    global list_count
    global tuple_count

    if isinstance(x, list):

        list_count += 1

        for i in x:
            count_types(i)

    elif isinstance(x, tuple):

        tuple_count += 1

        for i in x:
            count_types(i)


count_types(a)

print("Lists :", list_count)
print("Tuples:", tuple_count)

