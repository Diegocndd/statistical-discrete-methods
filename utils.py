import math

def binomial_coef(a, b):
    return math.factorial(a) / (math.factorial(b) * math.factorial(a - b))

def count_nodes_at_level(tree, level):
    if level == 0:
        return 1
    count = 0
    for child in tree.get('children', []):
        count += count_nodes_at_level(child, level - 1)
    return count

def buildTree(max_level, level, father_name, tree, all_posibilities = []):
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

    buildTree(max_level, level + 1, subtreeName1, subtree1, all_posibilities)
    buildTree(max_level, level + 1, subtreeName2, subtree2, all_posibilities)
