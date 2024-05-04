#!/usr/bin/python3
"""
Chamge comes from within
"""
def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    """
    # Sort coins in descending order to prioritize larger coins
    coins.sort(reverse=True)
    
    # Initialize a dictionary to store the minimum number of coins needed for each amount
    dp = {0: 0}
    
    for coin in coins:
        # Calculate the minimum number of coins needed for each amount starting from the coin value
        for i in range(coin, total + 1):
            # Only update dp[i] if it hasn't been calculated yet or if the new calculation results in fewer coins
            if i not in dp or dp[i] > dp[i - coin] + 1:
                dp[i] = dp[i - coin] + 1
                
    return dp[total] if total in dp else -1
