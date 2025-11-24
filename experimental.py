from las_vegas_max_3sat import las_vegas_max_3sat
from Reading import load_dimacs_file
import time

def run_experiments(test_files, num_runs=100):
    """
    Run multiple experiments on given test files to collect statistics.
    
    Args:
        test_files: List of file paths to test
        num_runs: Number of times to run the algorithm on each file
    
    Returns:
        Dictionary with statistics for each file
    """
    results = {}
    
    for test_file in test_files:
        # print(f"\n{'='*50}")
        print(f"Testing: {test_file}")
        # print(f"{'='*50}")
        
        try:
            n, clauses = load_dimacs_file(test_file)
            # print(f"Variables: {n}, Clauses: {len(clauses)}")
            
            ratios = []
            attempts_list = []
            times = []
            
            for run in range(num_runs):
                start = time.time()
                sol, score, attempts = las_vegas_max_3sat(n, clauses)
                duration = time.time() - start
                
                ratio = score / len(clauses)
                ratios.append(ratio)
                attempts_list.append(attempts)
                times.append(duration)
            
            # Calculate statistics
            avg_ratio = sum(ratios) / len(ratios)
            min_ratio = min(ratios)
            max_ratio = max(ratios)
            
            avg_attempts = sum(attempts_list) / len(attempts_list)
            min_attempts = min(attempts_list)
            max_attempts = max(attempts_list)
            
            avg_time = sum(times) / len(times)
            min_time = min(times)
            max_time = max(times)
            
            # Display results we have a lot
            # print(f"\nResults over {num_runs} runs:")
            # print(f"  Satisfaction ratio:")
            # print(f"    Average: {avg_ratio:.4f} ({avg_ratio*100:.2f}%)")
            # print(f"    Min: {min_ratio:.4f}, Max: {max_ratio:.4f}")
            # print(f"    >= 7/8 (87.5%)? {'YES' if avg_ratio >= 0.875 else 'NO'}")
            # print(f"  Attempts (iterations):")
            # print(f"    Average: {avg_attempts:.2f}")
            # print(f"    Min: {min_attempts}, Max: {max_attempts}")
            # print(f"  Running time:")
            # print(f"    Average: {avg_time:.6f} seconds")
            # print(f"    Min: {min_time:.6f}s, Max: {max_time:.6f}s")
            
            # Store results
            results[test_file] = {
                'num_vars': n,
                'num_clauses': len(clauses),
                'ratios': ratios,
                'avg_ratio': avg_ratio,
                'min_ratio': min_ratio,
                'max_ratio': max_ratio,
                'attempts': attempts_list,
                'avg_attempts': avg_attempts,
                'min_attempts': min_attempts,
                'max_attempts': max_attempts,
                'times': times,
                'avg_time': avg_time,
                'min_time': min_time,
                'max_time': max_time
            }
            
        except FileNotFoundError:
            print(f"Error: File '{test_file}' not found.")
            continue
    
    return results

def print_summary(results):
    """Print aggregated statistics across all test files"""
    print("\n" + "=" * 50)
    print("SUMMARY ACROSS ALL TEST FILES")
    print("=" * 50)
    
    all_avg_ratios = [r['avg_ratio'] for r in results.values()]
    all_avg_attempts = [r['avg_attempts'] for r in results.values()]
    all_avg_times = [r['avg_time'] for r in results.values()]
    
    print(f"Total files tested: {len(results)}")
    print(f"\nOverall satisfaction ratio:")
    print(f"  Average: {sum(all_avg_ratios)/len(all_avg_ratios):.4f}")
    print(f"  Min: {min(all_avg_ratios):.4f}, Max: {max(all_avg_ratios):.4f}")
    print(f"  Files with ratio >= 7/8: {sum(1 for r in all_avg_ratios if r >= 0.875)}/{len(all_avg_ratios)}")
    print(f"\nOverall attempts:")
    print(f"  Average: {sum(all_avg_attempts)/len(all_avg_attempts):.2f}")
    print(f"\nOverall running time:")
    print(f"  Average: {sum(all_avg_times)/len(all_avg_times):.6f} seconds")
