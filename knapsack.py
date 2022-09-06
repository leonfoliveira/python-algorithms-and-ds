from collections import defaultdict

# Returns the maximum sum of values with total weight less than or equal to capacity
def knapsack(values, weights, capacity):
	dp = defaultdict(int)
	
	for index, value in enumerate(values):
		weight = weights[index]
		for partial in range(capacity + 1):
			if weight > partial:
				dp[(index, partial)] = dp[(index - 1, partial)]
			else:
				dp[(index, partial)] = max(dp[(index - 1, partial)], value + dp[(index - 1, partial - weight)])
	
	return dp[(len(values) - 1, capacity)]

print(knapsack([60, 100, 120], [10, 20, 30], 50))
