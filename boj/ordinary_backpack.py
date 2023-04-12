N, K = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
items_list = []
for _ in range(N):
    weight, value = map(int, input().split())
    items_list.append((weight, value))

for item_index in range(1, N+1):
    for weight_capacity in range(1, K+1):
        weight, value = items_list[item_index-1]
        if weight <= weight_capacity:
            dp[item_index][weight_capacity] = max(dp[item_index-1][weight_capacity], dp[item_index-1][weight_capacity-weight] + value)
        else:
            dp[item_index][weight_capacity] = dp[item_index-1][weight_capacity]

print(dp[N][K])

# Updated with the help of GPT (Variable naming)
