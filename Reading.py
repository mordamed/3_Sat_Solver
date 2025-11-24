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
            
            # Reading literals (remove the final 0)
            literals = [int(x) for x in line.split() if x != '0']
            if literals:
                clauses.append(literals)
                
    return num_vars, clauses

def parse_dimacs_line(line):
    """Extracts literals from a DIMACS file line."""
    parts = line.split()
    # We ignore the final '0' if present and convert to int
    return [int(x) for x in parts if x not in ('0', '%')]