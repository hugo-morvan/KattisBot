# Various utility functions for the text mining project

def write_solution(file_path, solution):
    with open(file_path, 'w', encoding='utf-8') as f: 
            f.write(solution)
    
#____________________________________________________________________________________    
            
def extract_code(text: str) -> str:
    # Find the first and last occurrence of ```
    start = text.find('```')
    if start == -1:
        return text  # Return original text if no triple backticks found
    
    # Find the second set of backticks
    end = text.find('```', start + 3)
    if end == -1:
        return text  # Return original text if closing backticks not found
    
    # Extract the code between the backticks
    # Skip any language identifier after the first backticks
    code_start = text.find('\n', start + 3)
    if code_start == -1 or code_start > end:
        return text  # Return original text if no newline found
        
    return text[code_start + 1:end].strip()

#____________________________________________________________________________________

def parse_desc(raw_text):
    """
    Given the raw text descitpion from the autokattis api response,
    return description, input_rec, output_rec, test_cases_tuples
    
    """
    splitted = raw_text.split('\n')
    try:
        input_index = splitted.index('Input')
        output_index = splitted.index('Output')
        test1 = splitted.index('Sample Input 1')
        
        description = " ".join([chunk.strip("   ") for chunk in splitted[0:input_index]])
        input_rec = " ".join([chunk.strip("   ") for chunk in splitted[input_index+1:output_index]])
        output_rec = " ".join([chunk.strip("   ") for chunk in splitted[output_index+1:test1]])
        
    except Exception: #goingincircles problem
        # no in/out requirement, its an interactive problem
        input_index = splitted.index('Interaction')
        output_index = splitted.index('Read')
        test1 = splitted.index('Read')

        description = " ".join([chunk.strip("   ") for chunk in splitted[0:input_index]])
        input_rec = " ".join([chunk.strip("   ") for chunk in splitted[input_index+1:output_index]])
        output_rec = " ".join([chunk.strip("   ") for chunk in splitted[output_index+1:test1]])
        
        
    #print(f"{output_rec=}")
    test_cases = " ".join(splitted[test1:])
    cleaned_test_cases = []
    for s in test_cases.split("    "):
        if "Sample" in s :
            pass
        elif len(s)==0: #remove empty string
            pass
        else:
            cleaned_test_cases.append(s)

    test_cases_tuples = []
    for i in range(len(cleaned_test_cases)):
        #print(f"{i=}")
        if i%2==0:
            test_cases_tuples.append((cleaned_test_cases[i], cleaned_test_cases[i+1]))
    #print(f"{test_cases_tuples=}")
    return description, input_rec, output_rec, test_cases_tuples

raw_desc = """
#Image by 
        Pattarisara Suvichanarakul (iStock); Used under license
      

An airline tracks costs of flights between $n$ different cities in a table. The
    cities are numbered from $1$ to $n$. In the table, the entry in
    $\textrm{row}~ i$ and
    $\textrm{column}~ j$
    represents the cost of a direct flight from $\textrm{city}~ i$ to $\textrm{city}~ j$. However, if there
    is no direct flight between these two cities, then a value of
    $-1$ is displayed in the
    table. A manager for the airline has decided that the table is
    too hard to read with all the $-1$ values; she does not like all the
    negativity. Instead, she would prefer a list of the flight
    prices for just the cities for which there are direct flights.
    Each entry in the list should specify the city from which the
    flight departs, the city at which the flight lands, and the
    price for the flight. The list should be sorted in increasing
    order by departure city, and if there is more than one flight
    departing from a city, then ties should be broken by the
    arrival city in increasing order. For example, the table on the
    left below should be turned into the list on the right. This
    matches the first sample input/output.



Input
The first line of input consists of an integer, $n$ ($2
    \leq n \leq 100$), the number of cities. This is
    followed by $n$ lines,
    each consisting of $n$
    space-separated integers, where the $j^{\text {th}}$ value on the
    $i^{\text {th}}$ line
    indicates the cost of the flight from $\textrm{city}~ i$ to $\textrm{city}~ j$. A value of
    $-1$ is used to indicate
    that there is no direct flight from $\textrm{city}~ i$ to $\textrm{city}~ j$. It is guaranteed
    that there is no direct flight departing from and arriving at
    the same city. All costs will be strictly positive integers
    less than $10\, 000$. It
    is guaranteed that there will be at least one direct flight
    represented in the table.
Output
The first line of output is the number of direct flights,
    $m$. This is to be
    followed by $m$ lines of
    the form $u$ $v$ $c$, indicating that there is a
    direct flight from $\textrm{city}~ u$ to $\textrm{city}~ v$ with a cost of
    $\textrm{of}~ c$. These
    must be printed in ascending order, sorted by departure city
    number with ties broken by the arrival city number.


Sample Input 1
Sample Output 1



4
-1 1 -1 2
9 -1 -1 -1
-1 3 -1 4
7 1 2 -1



8
1 2 1
1 4 2
2 1 9
3 2 3
3 4 4
4 1 7
4 2 1
4 3 2







Sample Input 2
Sample Output 2



3
-1 -1 -1
15 -1 -1
2 2 -1



3
2 1 15
3 1 2
3 2 2
"""

# Testing function: 
# description, input_rec, output_rec, test_cases_tuples = parse_desc(raw_desc)
# print(f"{description=}")
# print(f"{input_rec=}")
# print(f"{output_rec=}")
# print(f"{test_cases_tuples=}")

#____________________________________________________________________________________

# Function to limit execution time
import concurrent.futures
import time

def run_with_timeout(func, timeout_seconds, *args, **kwargs):
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(func, *args, **kwargs)
        try:
            result = future.result(timeout=timeout_seconds)  # Set timeout
            return result
        except concurrent.futures.TimeoutError:
            return f"Function execution exceeded {timeout_seconds} seconds."
        
# Example usage
def long_running_task():
    print("Task started...")
    time.sleep(10)  # Simulate long task (e.g., 2 minutes)
    print("Task completed.")

result = run_with_timeout(long_running_task, 11)  # Timeout after 2 minutes
print(result)