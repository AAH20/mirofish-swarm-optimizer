"""MiroFish Swarm Optimizer Engine Facade."""
from typing import List, Dict, Tuple, Any, Optional
from .core.models import (
    SwarmAgent, CoalitionStructureResult, InfluenceResult, ConsensusRankingResult
)
from .core.coalition_structure import OptimalCoalitionStructureSolver
from .core.influence_maximizer import InfluenceMaximizer
from .core.kemeny_consensus import KemenyConsensusSolver
from .core.topology_sparsifier import TopologySparsifier
from .adapters.geopolitical import run_geopolitical_benchmark, build_geopolitical_agents
from .adapters.financial_markets import run_financial_benchmark, build_financial_agents

class MiroFishSwarmEngine:
    """
    Unified Optimization Engine for MiroFish-Scale Swarm Intelligence Simulation.
    Solves core NP-Hard problems with provable guarantees, exceeding Evolutionary Algorithm baselines.
    """

    def solve_optimal_coalitions(self, agents: List[SwarmAgent]) -> CoalitionStructureResult:
        solver = OptimalCoalitionStructureSolver(agents)
        return solver.solve()

    def solve_critical_influence(
        self,
        agents: List[SwarmAgent],
        network: Dict[str, List[Tuple[str, float]]],
        k_seeds: int = 3
    ) -> InfluenceResult:
        solver = InfluenceMaximizer(agents, network)
        return solver.solve(k_seeds=k_seeds)

    def solve_kemeny_consensus(
        self,
        outcomes: List[str],
        agent_rankings: List[List[str]]
    ) -> ConsensusRankingResult:
        solver = KemenyConsensusSolver(outcomes)
        return solver.solve(agent_rankings)

    def sparsify_topology(self, agents: List[SwarmAgent], max_degree: int = 4) -> Dict[str, Any]:
        sparsifier = TopologySparsifier(agents)
        return sparsifier.sparsify(max_degree=max_degree)

    def run_geopolitical_benchmark(self) -> Dict[str, Any]:
        return run_geopolitical_benchmark()

    def run_financial_benchmark(self) -> Dict[str, Any]:
        return run_financial_benchmark()
