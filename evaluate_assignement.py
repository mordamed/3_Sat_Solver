def evaluate_assignment(assignment, clauses):
    """
    Counts the number of clauses satisfied by the assignment.
    assignment: list of booleans (index 0 are ignored to keep indexing)
    """
    satisfied_count = 0
    for clause in clauses:
        is_clause_sat = False
        for literal in clause:
            var_index = abs(literal)
            val = assignment[var_index]
            
            # We put True for positive literal, False for negative
            # If literal > 0, we want val to be True
            # If literal < 0, we want val to be False
            # So when we meet this condition, the clause is satisfied
            if (literal > 0 and val) or (literal < 0 and not val):
                is_clause_sat = True
                break
        
        if is_clause_sat:
            satisfied_count += 1
    return satisfied_count