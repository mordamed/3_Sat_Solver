import random
from evaluate_assignement import evaluate_assignment

def las_vegas_max_3sat(num_vars, clauses):
    """
    Algorithme de Las Vegas pour Max 3-SAT.
    Garantit de satisfaire au moins 7/8 des clauses.
    """
    m = len(clauses)
    target = (7.0 / 8.0) * m
    attempts = 0
    
    while True:
        attempts += 1
        # 1. Générer une assignation aléatoire
        # On utilise une liste de taille num_vars + 1 pour indexer directement par 1..n
        assignment = [False] * (num_vars + 1)
        for i in range(1, num_vars + 1):
            assignment[i] = random.choice([True, False])
            
        # 2. Vérifier la condition
        score = evaluate_assignment(assignment, clauses)
        
        # 3. Si le score est >= 7/8 du total, on retourne le résultat
        if score >= target:
            return assignment, score, attempts