To solve this problem, we need to calculate the probabilities of each player rolling a higher sum than the other. Given the properties of the dice, we can use combinatorial methods to determine the number of ways each player can roll a specific sum and then compute the probability.

Here's a step-by-step approach to solve the problem:

1. **Define the Dice**: Each die has numbers from \(a_i\) to \(b_i\). We need to calculate the number of ways to roll each possible sum for both players.

2. **Calculate Sums**: For each die, calculate the possible sums and the number of ways to achieve each sum.

3. **Determine Probabilities**: For each possible sum that Gunnar can roll, calculate the probability that Emma can roll a lower sum. Similarly, for each possible sum that Emma can roll, calculate the probability that Gunnar can roll a lower sum.

4. **Compare Probabilities**: Sum up the probabilities for each player to determine which player has a higher chance of winning.

Here's the Python code to implement this:

```python
def count_ways_to_roll_sum(a, b, target):
    # Calculate the number of ways to roll a specific sum
    count = 0
    for i in range(a, b + 1):
        for j in range(a, b + 1):
            if i + j == target:
                count += 1
    return count

def calculate_probabilities(a1, b1, a2, b2):
    # Calculate the number of ways to roll each sum for Gunnar's die
    gunnar_ways = [count_ways_to_roll_sum(a1, b1, i) for i in range(2 * a1, 2 * b1 + 1)]
    
    # Calculate the number of ways to roll each sum for Emma's die
    emma_ways = [count_ways_to_roll_sum(a2, b2, i) for i in range(2 * a2, 2 * b2 + 1)]
    
    # Calculate the total number of ways to roll sums for both players
    total_gunnar_ways = sum(gunnar_ways)
    total_emma_ways = sum(emma_ways)
    
    # Calculate the probabilities
    prob_gunnar_win = 0
    prob_emma_win = 0
    
    for gunnar_sum in gunnar_ways:
        for emma_sum in em