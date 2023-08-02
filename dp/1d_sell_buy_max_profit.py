# a[i] - price
# each day or sell or buy
# find max possible profit

def max_profit(prices: list[int]) -> int:
  n = len(prices)
  # states
  # base
  min_price = prices[0]
  max_profit = 0

  # move
  for i in range(0, n, 1):
    # formula
    cost = prices[i] - min_price
    max_profit = max(max_profit, cost)
    min_price = min(min_price, prices[i])

  # result
  return max_profit


print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))
