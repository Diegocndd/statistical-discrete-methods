import math

from utils import *

def bernoulli(successRate, sampleSize):
    all_posibilities = []

    failureRate = 1 - successRate

    tree = { 'name': '.', 'children': [], 'level': 0 }

    buildTree(
        max_level=sampleSize,
        level=1,
        father_name='',
        tree=tree,
        all_posibilities=all_posibilities
    )

    # occurrences of success
    k = 1

    print('------- Bernoulli Method --------------------')

    print('Occurrences of success: ', k)
    print('Number of attempts: ', sampleSize)

    # brute force
    total = 1
    arr = [p for p in all_posibilities if p.count('s') == k]

    first = arr[0]

    for i in first:
        if i == 'f':
            total *= failureRate
        else:
            total *= successRate

    print('Probability by brute force: ', total * len(arr))

    # by bernoulli method formule
    res = binomial_coef(sampleSize, k) * math.pow(successRate, k) * math.pow(failureRate, sampleSize - k)
    print('Probabilty by direct formula: ', res)