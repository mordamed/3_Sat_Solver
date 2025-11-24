# Max 3-SAT Las Vegas Algorithm

A Las Vegas randomized algorithm that guarantees to satisfy at least 7/8 of the clauses in any Max 3-SAT instance.

## Files

- `las_vegas_max_3sat.py` - Main algorithm implementation
- `evaluate_assignement.py` - Function to evaluate clause satisfaction
- `Reading.py` - DIMACS CNF file parser
- `experimental.py` - Experimental framework for running multiple tests
- `main.py` - Main entry point

## Usage

```bash
python main.py
```

The program will:
1. Run a simple example
2. Test all instances in the `uf20-91/` directory
3. Display statistics for each file

## Algorithm

The algorithm repeatedly generates random boolean assignments until it finds one that satisfies at least 7/8 of the clauses. Since each clause has 3 literals, a random assignment satisfies any clause with probability 7/8, guaranteeing success.

## Benchmarks

Test instances from SATLIB: https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html
- `uf20-91/`: 20 variables, 91 clauses (uniform random satisfiable instances)
