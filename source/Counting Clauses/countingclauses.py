m, n = map(int, input().split())
clauses = [tuple(map(int, input().split())) for _ in range(m)]

def is_satisfiable(clauses):
    from itertools import product

    # Generate all possible assignments of True/False to variables
    for assignment in product([True, False], repeat=n):
        # Check if the current assignment satisfies all clauses
        if all(any(assignment[var] if lit > 0 else not assignment[var] for var, lit in clause) for clause in clauses):
            return True
    return False

if is_satisfiable(clauses):
    print("satisfactory")
else:
    print("unsatisfactory")