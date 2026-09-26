"""MiroFish Swarm Optimizer: Hard Mathematical Solvers for Swarm Intelligence Simulation."""
from .core.models import (
    SwarmAgent, AgentFaction, Coalition, CoalitionStructureResult,
    InfluenceResult, ConsensusRankingResult, BenchmarkComparison
)
from .core.coalition_structure import OptimalCoalitionStructureSolver
from .core.influence_maximizer import InfluenceMaximizer
from .core.kemeny_consensus import KemenyConsensusSolver
from .core.topology_sparsifier import TopologySparsifier
from .core.evolutionary_baselines import GeneticAlgorithmCSG, ParticleSwarmInfluenceMaximizer
from .engine import MiroFishSwarmEngine
from .adapters.geopolitical import run_geopolitical_benchmark, build_geopolitical_agents
from .adapters.financial_markets import run_financial_benchmark, build_financial_agents

__version__ = "1.0.0"

__all__ = [
    "SwarmAgent",
    "AgentFaction",
    "Coalition",
    "CoalitionStructureResult",
    "InfluenceResult",
    "ConsensusRankingResult",
    "BenchmarkComparison",
    "OptimalCoalitionStructureSolver",
    "InfluenceMaximizer",
    "KemenyConsensusSolver",
    "TopologySparsifier",
    "GeneticAlgorithmCSG",
    "ParticleSwarmInfluenceMaximizer",
    "MiroFishSwarmEngine",
    "run_geopolitical_benchmark",
    "build_geopolitical_agents",
    "run_financial_benchmark",
    "build_financial_agents",
]
