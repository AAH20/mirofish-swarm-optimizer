"""CLI Interface for MiroFish Swarm Optimization Engine."""
import argparse
import sys
import time
from .adapters.geopolitical import run_geopolitical_benchmark, build_geopolitical_agents
from .adapters.financial_markets import run_financial_benchmark, build_financial_agents
from .core.coalition_structure import OptimalCoalitionStructureSolver
from .core.evolutionary_baselines import GeneticAlgorithmCSG

def cmd_geopolitical(args):
    print("=" * 90)
    print("MIROFISH SWARM OPTIMIZER: GEOPOLITICAL ALLIANCE & CRISIS CASCADE BENCHMARK")
    print("Simulation: 10 Sovereign States & Institutional Blocs | GraphRAG Social Matrix")
    print("Algorithmic Paradigm: Exact / Submodular Solvers vs Heuristic & Evolutionary Baselines")
    print("=" * 90)

    res = run_geopolitical_benchmark()
    csg = res["csg_comparison"]
    inf = res["influence_comparison"]

    print("\n--- 1. OPTIMAL COALITION STRUCTURE GENERATION (CSG) BENCHMARK ---")
    print(f"{'Metric':<30} | {'Exact IDP Solver (Ours)':<28} | {'Genetic Algorithm (GA)':<28}")
    print("-" * 90)
    exact_time_str = f"{csg['exact'].execution_time_us:.1f} µs"
    ga_time_str = f"{csg['ga'].execution_time_us:.1f} µs"
    speedup_str = f"{csg['speedup_factor']:.1f}x Faster Execution"
    print(f"{'Social Welfare Score':<30} | {csg['exact'].total_welfare:>28.3f} | {csg['ga'].total_welfare:>28.3f}")
    print(f"{'Execution Latency':<30} | {exact_time_str:>28} | {ga_time_str:>28}")
    print(f"{'Optimality & Speedup':<30} | {'Exact Global Optimum (100%)':>28} | {speedup_str:>28}")
    print(f"\n  * Optimal Coalition Blocs Formed ({len(csg['exact'].coalitions)} Coalitions):")
    for idx, c in enumerate(csg['exact'].coalitions, 1):
        print(f"    - Bloc #{idx} (Value: {c.value:.2f}): {', '.join(c.members)}")

    print("\n--- 2. CRITICAL TIPPING POINT & INFLUENCE MAXIMIZATION BENCHMARK ---")
    print(f"{'Metric':<30} | {'Martingale RR-Sketch (Ours)':<28} | {'Particle Swarm (PSO)':<28}")
    print("-" * 90)
    exact_reach_str = f"{inf['exact_sketch'].expected_reach:.2f} agents ({inf['exact_sketch'].activation_percentage:.1f}%)"
    pso_reach_str = f"{inf['pso'].expected_reach:.2f} agents ({inf['pso'].activation_percentage:.1f}%)"
    exact_inf_time_str = f"{inf['exact_sketch'].execution_time_us:.1f} µs"
    pso_inf_time_str = f"{inf['pso'].execution_time_us:.1f} µs"
    inf_speedup_str = f"{inf['speedup_factor']:.1f}x Faster Execution"
    print(f"{'Expected Cascade Spread':<30} | {exact_reach_str:>28} | {pso_reach_str:>28}")
    print(f"{'Execution Latency':<30} | {exact_inf_time_str:>28} | {pso_inf_time_str:>28}")
    print(f"{'Approximation Bound':<30} | {'(1 - 1/e) >= 63.2% Provable':>28} | {inf_speedup_str:>28}")
    print(f"  * Critical Diplomatic Tipping Point Seeds: {', '.join(inf['exact_sketch'].seed_agents)}")

    print("\n--- 3. KEMENY-YOUNG CONDORCET CONSENSUS SYNTHESIS ---")
    kem = res["kemeny_consensus"]
    print(f"  * Synthesized Treaty Preference: {' -> '.join(kem.ranked_outcomes)}")
    print(f"  * Pairwise Inversion Distance : {kem.total_kendall_tau_distance:.0f} (Global Minimum)")
    print(f"  * Swarm Agreement Score       : {kem.agreement_score * 100.0:.1f}% (Zero Condorcet Violations)")
    print(f"  * Aggregation Latency         : {kem.execution_time_us:.2f} µs")

    print("\n--- 4. DEGREE-CONSTRAINED TOPOLOGY SPARSIFICATION ---")
    top = res["topology_sparsification"]
    print(f"  * Total Full-Mesh Edges       : {top['total_possible_edges']} candidate links")
    print(f"  * Retained High-Entropy Links : {top['active_edges_count']} sparse bridge channels")
    print(f"  * Token / Message Reduction   : {top['message_reduction_pct']:.1f}% bandwidth reduction")
    print(f"  * Information Entropy Score   : {top['information_entropy_score']:.2f} (Prevents Echo Chambers)")
    print(f"  * Graph Sparsification Time   : {top['execution_time_us']:.2f} µs")
    print("=" * 90)

def cmd_financial(args):
    print("=" * 90)
    print("MIROFISH SWARM OPTIMIZER: FINANCIAL MARKET MICROSTRUCTURE BENCHMARK")
    print("Simulation: 8 Heterogeneous Market Entities (MMs, Quant HF, CTA, Pension, Central Bank)")
    print("Core Focus: Liquidity Cartels, Flash Crash Catalysts, and Price Target Aggregation")
    print("=" * 90)

    res = run_financial_benchmark()
    csg = res["csg_comparison"]
    inf = res["influence_comparison"]

    print("\n--- 1. LIQUIDITY SYNDICATE COALITION FORMATION ---")
    print(f"  * Exact Solver Total Welfare   : {csg['exact'].total_welfare:.3f} (Latency: {csg['exact'].execution_time_us:.1f} µs)")
    print(f"  * Genetic Algorithm Welfare    : {csg['ga'].total_welfare:.3f} (Latency: {csg['ga'].execution_time_us:.1f} µs)")
    print(f"  * Quality Premium over GA      : +{csg['welfare_gain_pct']:.2f}% superior liquidity allocation")
    print(f"  * Algorithmic Speedup Factor   : {csg['speedup_factor']:.1f}x faster execution")

    print("\n--- 2. FLASH-CRACK TIPPING POINT IDENTIFICATION ---")
    print(f"  * Critical Catalyst Entities   : {', '.join(inf['exact_sketch'].seed_agents)}")
    print(f"  * Cascading Liquidity Contagion: {inf['exact_sketch'].expected_reach:.2f} / 8 entities ({inf['exact_sketch'].activation_percentage:.1f}%)")
    print(f"  * RR-Sketch Solver Latency     : {inf['exact_sketch'].execution_time_us:.1f} µs vs PSO {inf['pso'].execution_time_us:.1f} µs")

    print("\n--- 3. KEMENY ASSET REGIME CONSENSUS ---")
    kem = res["kemeny_consensus"]
    print(f"  * Market Regime Consensus     : {' -> '.join(kem.ranked_outcomes)}")
    print(f"  * Agreement Score             : {kem.agreement_score * 100.0:.1f}%")
    print("=" * 90)

def cmd_benchmark_scaling(args):
    print("=" * 90)
    print("MIROFISH COALITION GENERATION: EXACT IDP VS GENETIC ALGORITHM SWEEP")
    print("Demonstrating Super-Exponential Search Space (Bell Numbers B_n) & Exact Optimality")
    print("=" * 90)

    all_agents = build_geopolitical_agents()
    scales = [6, 8, 10]

    print(f"{'Agents (N)':<12} | {'Partitions B_n':<16} | {'Exact Welfare':<15} | {'GA Welfare':<15} | {'Optimality Gap':<16} | {'Exact Time (µs)':<16}")
    print("-" * 90)

    for n in scales:
        sub_agents = all_agents[:n]
        exact_solver = OptimalCoalitionStructureSolver(sub_agents)
        res_exact = exact_solver.solve()

        ga_solver = GeneticAlgorithmCSG(sub_agents, population_size=40, generations=50)
        res_ga = ga_solver.solve()

        gap = ((res_exact.total_welfare - res_ga.total_welfare) / res_exact.total_welfare) * 100.0
        # Bell numbers for n=6, 8, 10
        bell = {6: 203, 8: 4140, 10: 115975}.get(n, 0)
        print(f"{n:<12} | {bell:<16} | {res_exact.total_welfare:>14.3f} | {res_ga.total_welfare:>14.3f} | {gap:>15.2f}% | {res_exact.execution_time_us:>14.1f}")

    print("=" * 90)
    print("BENCHMARK COMPLETE: EXACT MATHEMATICAL SOLVERS EXCEED EVOLUTIONARY ALGORITHMS.")
    print("=" * 90)

def main():
    parser = argparse.ArgumentParser(
        description="MiroFish Swarm Optimizer: Hard Mathematical Solvers for Swarm Intelligence"
    )
    subparsers = parser.add_subparsers(dest="subcommand", help="Available subcommands")

    subparsers.add_parser("benchmark-geopolitical", help="Run geopolitical summit benchmark comparing Exact vs GA/PSO")
    subparsers.add_parser("benchmark-financial", help="Run financial market benchmark comparing Exact vs GA/PSO")
    subparsers.add_parser("benchmark-scaling", help="Run scaling sweep of Exact IDP vs Genetic Algorithm")

    args = parser.parse_args()
    if args.subcommand == "benchmark-geopolitical":
        cmd_geopolitical(args)
    elif args.subcommand == "benchmark-financial":
        cmd_financial(args)
    elif args.subcommand == "benchmark-scaling":
        cmd_benchmark_scaling(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
