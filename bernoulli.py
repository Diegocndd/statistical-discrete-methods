import math

all_posibilities = []

def binomial_coef(a, b):
    return math.factorial(a) / (math.factorial(b) * math.factorial(a - b))

def count_nodes_at_level(tree, level):
    if level == 0:
        return 1
    count = 0
    for child in tree.get('children', []):
        count += count_nodes_at_level(child, level - 1)
    return count

def buildTree(max_level, level, father_name, tree):
    global all_posibilities
    # s for success / f for failure
    subtreeName1 = father_name + 's'
    subtreeName2 = father_name + 'f'
    subtree1 = { 'name': subtreeName1, 'children': [], 'level': level }
    subtree2 = { 'name': subtreeName2, 'children': [], 'level': level }

    tree['children'].append(subtree1)
    tree['children'].append(subtree2)

    if (level + 1 > max_level):
        all_posibilities.append(subtreeName1)
        all_posibilities.append(subtreeName2)
        return

    buildTree(max_level, level + 1, subtreeName1, subtree1)
    buildTree(max_level, level + 1, subtreeName2, subtree2)

successRate = 0.8
failureRate = 1 - successRate
sampleSize = 10

tree = { 'name': '.', 'children': [], 'level': 0 }

buildTree(
    max_level=sampleSize,
    level=1,
    father_name='',
    tree=tree
)


# occurrences of success
k = 1

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