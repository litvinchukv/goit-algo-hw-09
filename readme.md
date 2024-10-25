
# Comparison of Greedy Algorithm and Dynamic Programming for Change Making Problem

## Problem Statement
Given a set of coins `[50, 25, 10, 5, 2, 1]`, we need to create a system for a cash register that can determine the optimal way to provide change to a customer. Two approaches were implemented:

1. **Greedy Algorithm (`find_coins_greedy`)**: Aims to use the largest available denominations first.
2. **Dynamic Programming (`find_min_coins`)**: Aims to find the minimal number of coins required to form the given sum.

## Example Case
For an example amount of `113`, both algorithms produce the following result:
- **Greedy Algorithm Output**: `{50: 2, 10: 1, 2: 1, 1: 1}`
- **Dynamic Programming Output**: `{50: 2, 10: 1, 2: 1, 1: 1}`

## Efficiency Comparison
1. **Greedy Algorithm**  
   - **Time Complexity**: O(n), where `n` is the number of different coin denominations.
   - **Behavior**: Iterates over each denomination starting from the largest. For each coin, it uses as many as possible before moving to the next smaller denomination.
   - **Performance**: Fast and efficient for most standard coin sets (canonical sets), like the one used in this example. However, it might not always provide the optimal solution for non-canonical sets.

2. **Dynamic Programming Algorithm**  
   - **Time Complexity**: O(n*m), where `n` is the number of different coin denominations and `m` is the amount.
   - **Behavior**: Iterates over all possible sums up to the given amount and considers each coin to ensure the minimal number of coins is used.
   - **Performance**: Guarantees an optimal solution regardless of the coin set. It may be slower than the greedy algorithm for large sums because it uses a double iteration (over the amount and the coins).

## Conclusion
- The **Greedy Algorithm** is generally more efficient in terms of time complexity for large sums when using a canonical coin set.
- The **Dynamic Programming Algorithm** is more versatile and provides an optimal solution for any coin set, but its time complexity makes it less efficient for very large amounts.

For the specific example given (`113`), both algorithms produce the same output as the coin set is canonical. However, in cases with non-canonical coin sets, the greedy approach might not provide the minimal number of coins, whereas the dynamic programming method will always find the optimal solution.
