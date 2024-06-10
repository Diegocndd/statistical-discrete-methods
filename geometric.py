from utils import *

import math 

def geometric(successRate, sampleSize) -> None:
    failureRate = 1 - successRate

    result = successRate * math.pow(failureRate, sampleSize)

    print('------- Geometric Method --------------------')

    print('Occurrences of failures before first success: ', sampleSize)
    print('Probability of this: ', result)
