#  Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and 
#bound strategy. 
def knapsack(values, weights, W):
    ratio = [v / w for v, w in zip(values, weights)]
    items = sorted(zip(ratio, values, weights), reverse=True)
    total, cap = 0, W
    for r, v, w in items:
        if cap >= w:
            total += v; cap -= w
        else:
            continue  # can't take item (0/1 rule)
    return total

v = [60, 100, 120]
w = [10, 20, 30]
print("Max profit =", knapsack(v, w, 50))

