def evaluate_assignment(assignment, clauses):
    """
    Compte le nombre de clauses satisfaites par l'assignation.
    assignment: liste de booléens (index 0 ignoré pour correspondre aux vars 1..n)
    """
    satisfied_count = 0
    for clause in clauses:
        is_clause_sat = False
        for literal in clause:
            var_index = abs(literal)
            val = assignment[var_index]
            
            # Si littéral positif (x), il faut que val soit True
            # Si littéral négatif (-x), il faut que val soit False
            if (literal > 0 and val) or (literal < 0 and not val):
                is_clause_sat = True
                break
        
        if is_clause_sat:
            satisfied_count += 1
    return satisfied_count