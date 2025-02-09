"""
Secretary Problem Simulation and Optimization

Author: Wilmer Leon
Contact: https://www.linkedin.com/in/wilmer-leon/

Description:
This script implements a simulation of the Secretary Problem, a classic optimal stopping problem.
The goal is to determine the optimal fraction of candidates to initially reject before selecting the first candidate
who is better than all previous ones. The program runs multiple simulations to find the optimal rejection fraction.

Additionally, this version includes a range of skip fractions, text-based tabular results, and visualizations using matplotlib.

Usage:
Run the script as follows:
    python secretary_problem.py

Operations:
- Simulates the Secretary Problem for a given number of candidates.
- Iterates over different rejection fractions to find the optimal one.
- Uses Monte Carlo simulations to determine success rates and average rankings.
- Generates a text-based table of results.
- Generates a plot visualizing success rates against skip fractions.

Dependencies:
- Python 3.7 or higher
- numpy (install via: pip install numpy)
- matplotlib (install via: pip install matplotlib)
- tqdm (install via: pip install tqdm)
"""

import random
import math
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def simulate_secretary(n, skip_fraction, iterations=10000):
    """
    Simulate the Secretary Problem for a given number of candidates (n)
    and a given skip fraction over a number of iterations.
    Returns the fraction of simulations where the best candidate was selected.
    """
    success_count = 0
    total_rank = 0
    r = int(n * skip_fraction)
    
    for _ in tqdm(range(iterations), desc=f"Skip fraction {skip_fraction:.3f}", leave=False):
        candidates = list(range(n))
        random.shuffle(candidates)
        best_candidate = n - 1
        best_so_far = max(candidates[:r]) if r > 0 else -1
        chosen = next((c for c in candidates[r:] if c > best_so_far), candidates[-1])
        if chosen == best_candidate:
            success_count += 1
        total_rank += chosen
    
    success_rate = success_count / iterations
    average_rank = total_rank / iterations
    return success_rate, average_rank

def main():
    """
    Run the Secretary Problem simulation for multiple skip fractions, display results in a table,
    and visualize the results.
    """
    n = 100
    iterations = 10000
    fractions = np.linspace(0.0, 1.0, 21)
    results = [(f, *simulate_secretary(n, f, iterations)) for f in fractions]
    
    optimal_index = np.argmax([r[1] for r in results])
    optimal_fraction = results[optimal_index][0]
    optimal_success_rate = results[optimal_index][1]
    optimal_avg_rank = results[optimal_index][2]
    
    print("\n--- Summary of Results ---")
    print("Rejection Fraction | Success Rate | Average Rank")
    print("-------------------|--------------|-------------")
    for fraction, success_rate, average_rank in results:
        print(f"{fraction:18.2f} | {success_rate:12.2f}% | {average_rank:11.2f}")
    
    print(f"\nOptimal Rejection Fraction: {optimal_fraction:.3f}")
    print(f"Optimal Success Rate: {optimal_success_rate:.3f}")
    print(f"Optimal Average Rank: {optimal_avg_rank:.3f}")
    print(f"Theoretical optimal fraction (1/e): {1/math.e:.3f}")
    
    plt.figure(figsize=(8, 5))
    plt.plot(fractions, [r[1] for r in results], marker='o', label="Simulated Success Rate")
    plt.axvline(x=1/math.e, color='red', linestyle='--', label=f"Theoretical 1/e ≈ {1/math.e:.3f}")
    plt.xlabel("Skip fraction (r/n)")
    plt.ylabel("Success Probability")
    plt.title("Secretary Problem Simulation")
    plt.legend()
    plt.grid(True)
    plt.pause(0.001)  # Allows the window to refresh
    input("Press Enter to close...")  # Waits for user input before closing
    plt.close()
    
if __name__ == "__main__":
    main()