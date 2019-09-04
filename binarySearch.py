import math



primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
xmin = 0
xmax = len(primes) - 1
target = 67
iteration = 0

def binarySearch(primes, xmin, xmax, target, iteration=0):
    for x in primes:
        iteration = iteration + 1
        arrVal = math.floor((xmin + xmax) / 2)
        if primes[arrVal] < target:
            xmin = arrVal + 1
        elif primes[arrVal] > target:
            xmax = arrVal - 1
        else:
            print("I found it in " + str(iteration)+ " tries. It's value " + str(primes[arrVal]) + " at index " + str(arrVal))
            break

binarySearch(primes, xmin, xmax, target, iteration)