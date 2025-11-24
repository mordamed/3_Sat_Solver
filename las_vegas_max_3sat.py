import random
from evaluate_assignement import evaluate_assignment

def las_vegas_max_3sat(num_vars, clauses):
    """
    Las Vegas algorithm for Max 3-SAT.
    Guarantees to satisfy at least 7/8 of the clauses.
    """
    m = len(clauses)
    target = (7.0 / 8.0) * m
    attempts = 0
    while True:
        attempts += 1
        # 1. Generate a random assignment
        # We use a list of size num_vars + 1 to index directly by 1..n
        assignment = [False] * (num_vars + 1)
        for i in range(1, num_vars + 1):
            assignment[i] = random.choice([True, False])
            
        # 2. Check the condition (number of satisfied clauses)
        score = evaluate_assignment(assignment, clauses)
        
        # 3. If the score is >= 7/8 of the total, return the result
        if score >= target:
            return assignment, score, attempts
