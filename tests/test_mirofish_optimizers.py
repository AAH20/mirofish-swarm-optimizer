"""Unit tests for MiroFish Swarm Optimization Engine."""
import unittest
from mirofish_swarm_optimizer.engine import MiroFishSwarmEngine
from mirofish_swarm_optimizer.core.models import SwarmAgent, AgentFaction
from mirofish_swarm_optimizer.core.coalition_structure import OptimalCoalitionStructureSolver
from mirofish_swarm_optimizer.core.influence_maximizer import InfluenceMaximizer
from mirofish_swarm_optimizer.core.kemeny_consensus import KemenyConsensusSolver
from mirofish_swarm_optimizer.core.topology_sparsifier import TopologySparsifier
from mirofish_swarm_optimizer.core.evolutionary_baselines import GeneticAlgorithmCSG, ParticleSwarmInfluenceMaximizer
from mirofish_swarm_optimizer.adapters.geopolitical import build_geopolitical_agents, build_geopolitical_influence_network

class TestMiroFishSwarmOptimizers(unittest.TestCase):

    def setUp(self):
        self.engine = MiroFishSwarmEngine()
        self.agents = build_geopolitical_agents()
        self.network = build_geopolitical_influence_network()

    def test_optimal_coalition_structure_vs_ga(self):
        # Test on 8 agents for fast deterministic test verification
        test_agents = self.agents[:8]
        exact_solver = OptimalCoalitionStructureSolver(test_agents)
        res_exact = exact_solver.solve()

        ga_solver = GeneticAlgorithmCSG(test_agents, population_size=30, generations=30)
        res_ga = ga_solver.solve()

        # Exact must find welfare >= GA
        self.assertGreaterEqual(res_exact.total_welfare, res_ga.total_welfare - 1e-4)

        # Verify exact partition covers all agents exactly once
        partitioned_agents = []
        for c in res_exact.coalitions:
            partitioned_agents.extend(c.members)
        self.assertEqual(sorted(partitioned_agents), sorted([a.agent_id for a in test_agents]))

    def test_influence_maximization_rr_sketch(self):
        inf_solver = InfluenceMaximizer(self.agents, self.network)
        res = inf_solver.solve(k_seeds=2, num_samples=500)

        self.assertEqual(len(res.seed_agents), 2)
        self.assertGreater(res.expected_reach, 0.0)
        self.assertLess(res.execution_time_us, 100000.0)  # Sub-100ms

    def test_kemeny_young_consensus(self):
        outcomes = ["OPT-A", "OPT-B", "OPT-C"]
        # Clear Condorcet preference: A > B > C by majority
        rankings = [
            ["OPT-A", "OPT-B", "OPT-C"],
            ["OPT-A", "OPT-B", "OPT-C"],
            ["OPT-B", "OPT-A", "OPT-C"],
        ]
        solver = KemenyConsensusSolver(outcomes)
        res = solver.solve(rankings)

        # Optimal Kemeny rank must be OPT-A first
        self.assertEqual(res.ranked_outcomes[0], "OPT-A")
        self.assertEqual(res.ranked_outcomes, ["OPT-A", "OPT-B", "OPT-C"])
        self.assertGreater(res.agreement_score, 0.5)

    def test_topology_sparsifier_connectivity_and_degrees(self):
        sparsifier = TopologySparsifier(self.agents)
        max_deg = 3
        res = sparsifier.sparsify(max_degree=max_deg)

        self.assertGreater(res["active_edges_count"], 0)
        self.assertGreater(res["message_reduction_pct"], 50.0)
        self.assertLessEqual(res["average_degree"], max_deg)

if __name__ == "__main__":
    unittest.main()
