from las_vegas_max_3sat import las_vegas_max_3sat
from Reading import load_dimacs_file
from experimental import run_experiments, print_summary
import os
import glob

if __name__ == "__main__":
    # Simple example with 4 variables and 5 clauses

    # print("=" * 50)
    # print("SIMPLE EXAMPLE")
    # print("=" * 50)
    # clauses_exemple = [
    #     [1, 2, 1, -3],      # x1 or x2 or not-x3
    #     [-1, -2, 3],        # not-x1 or not-x2 or x3
    #     [2, -3, 4],         # x2 or not-x3 or x4
    #     [-2, 3, -4],
    #     [1, 3, 4]
    # ]
    # nb_variables = 4

    # print("Searching for a solution satisfying >= 7/8 of the clauses...")
    # solution, score, nb_essais = las_vegas_max_3sat(nb_variables, clauses_exemple)

    # print(f"Success in {nb_essais} attempt(s)!")
    # print(f"Clauses satisfied: {score}/{len(clauses_exemple)}")
    # print(f"Final assignment: {solution[1:]}") # We ignore index 0

    # Run experiments on SATLIB benchmarks
    print("\n" + "=" * 50)
    print("EXPERIMENTS ON SATLIB BENCHMARKS")
    print("=" * 50)
    
    # Get all .cnf files from uf20-91 directory
    test_files = glob.glob("./uf20-91/*.cnf")
    print(f"Found {len(test_files)} test files")
    num_runs = 100
    
    results = run_experiments(test_files, num_runs)

    print_summary(results)