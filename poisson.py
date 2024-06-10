from utils import *

import math 

def poisson(numEvents, knownFrequency, interval = 1):
    print('------- Poisson Method --------------------')

    print('Known frequency: ', knownFrequency)
    print('New number of events: ', numEvents)
    print('Interval: ', interval)

    sampleSize = 10000
    result = binomial_coef(sampleSize, numEvents) * math.pow(knownFrequency * (interval / sampleSize), numEvents) * math.pow((1 - (knownFrequency * interval / sampleSize)), sampleSize - numEvents)

    print(f'Using brute force (n = {sampleSize}): ', result)

    result = (math.pow(math.e, -1 * knownFrequency) * math.pow(knownFrequency, numEvents)) / math.factorial(numEvents)

    print('Using direct formula (n -> ∞): ', result)

    return result
