#!/usr/bin/python3

def missing_number(array1, array2):
    missing_no = 0

    for item in array1+array2:
        missing_no ^= item

    return missing_no


m = missing_number([1, 2, 3, 7, 7], [3, 7, 2, 1])

print ("Missing Number - " + str(m))

