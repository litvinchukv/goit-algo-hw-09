# I'll start by implementing both functions: find_coins_greedy and find_min_coins.

def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    """
    Greedy algorithm to find the optimal way to give change.
    It takes the largest available denomination and uses as many as possible
    before moving to the next smaller denomination.
    """
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    """
    Dynamic programming algorithm to find the minimal number of coins
    required to make the change for the given amount.
    """
    # Initialize DP array where dp[i] represents the minimum number of coins to make sum i.
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # base case: zero coins to make sum 0

    # Array to track the coin choices that form the optimal solution.
    coin_used = [0] * (amount + 1)

    # Fill the DP array
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Build the result dictionary from the coin_used array.
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result
if __name__ == "__main__":
    # Test cases to compare both algorithms
    amount_test = 113

    # Results from both algorithms
    greedy_result = find_coins_greedy(amount_test)
    dp_result = find_min_coins(amount_test)

    print(greedy_result)
    print(dp_result)