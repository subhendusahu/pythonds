#!/usr/bin/python3

def largest_seq_sum(seq):
    max_sum = seq[0] 
    temp_sum = seq[0]

    if len(seq) == 1:
        return max_sum

    for s in seq[1:]:
        temp_sum = max(temp_sum+s, s)
        max_sum = max(temp_sum, max_sum)

    return max_sum

l = largest_seq_sum([1, 2, -1, -3, 6, 6, -2, -11, -9, 10])

print ("Largest Sum - " + str(l))
