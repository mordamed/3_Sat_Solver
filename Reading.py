def load_dimacs_file(filepath):
    clauses = []
    num_vars = 0

    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('c') or line.startswith('%'):
                continue
            
            if line.startswith('p'):
                parts = line.split()
                num_vars = int(parts[2])
                continue
            
            # Lecture des littéraux (on enlève le 0 final)
            literals = [int(x) for x in line.split() if x != '0']
            if literals:
                clauses.append(literals)
                
    return num_vars, clauses

def parse_dimacs_line(line):
    """Extrait les littéraux d'une ligne de fichier DIMACS."""
    parts = line.split()
    # On ignore le '0' final s'il est présent et on convertit en int
    return [int(x) for x in parts if x not in ('0', '%')]