#!/usr/bin/python3

import sys 

def num_of_coins(cents):
    #defined_coins = [25, 10, 5, 1]
    if cents < 1:
        return 0

    defined_coins1 = [25, 5, 1]
    defined_coins2 = [5, 25, 1]
    no_of_coins = cents % 5
    cents -= no_of_coins

    if cents % 10 in [1, 2, 3 ,4] :
        for coin in defined_coins2:
            no_of_coins += cents // coin
            cents = cents % coin
    else:
        for coin in defined_coins1:
            no_of_coins += cents // coin
            cents = cents % coin
            if cents == 0:
                break
 
    return no_of_coins


c = num_of_coins(int(sys.argv[1]))

print ("Number of coins - " + str(c))
