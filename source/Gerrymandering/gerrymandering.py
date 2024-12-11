To solve this problem, we need to process the input data to determine the winner of each district, calculate the wasted votes for each party, and then compute the efficiency gap. Here's a step-by-step breakdown of how to implement this:

1. **Parse the Input**: Read the number of precincts `P` and districts `D`, followed by the details of each precinct.

2. **Group Precincts by District**: Use a dictionary to group precincts by their respective districts.

3. **Calculate Votes for Each Party in Each District**:
   - For each district, sum the votes for party A and party B.
   - Determine the winner based on the total votes for each party.

4. **Calculate Wasted Votes**:
   - For each district, calculate the wasted votes for party A and party B using the defined rules.

5. **Compute Efficiency Gap**:
   - Sum the wasted votes for both parties across all districts.
   - Calculate the efficiency gap using the formula provided.

6. **Output the Results**:
   - Print the winner for each district.
   - Print the wasted votes for each party in each district.
   - Print the efficiency gap.

Here's the Python code implementing the above logic:

```python
def calculate_wasted_votes(a_votes, b_votes):
    total_votes = a_votes + b_votes
    if total_votes == 0:
        return 0, 0
    
    threshold = (total_votes + 1) // 2
    lost_votes = a_votes if a_votes < b_votes else b_votes
    excess_votes = max(0, a_votes - threshold) if a_votes > b_votes else max(0, b_votes - threshold)
    
    return lost_votes, excess_votes

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    P = int(data[0])
    D = int(data[1])
    precincts = []
    
    # Parse precinct data
    for i in range(P):
        precincts.append((int(data[i * 3 + 2]), int(data[i * 3 + 1]), int(data[i * 3])))
    
    # Group precincts by district
    district_precincts = {}
    for precinct in precincts:
        district = precinct[2]
        if district not in district_precincts:
            district_precincts[district] = []
        district_precincts[district].append(precinct)
    
