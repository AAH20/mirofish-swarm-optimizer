"""Core models and data structures for MiroFish Swarm Optimization."""
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Set, Tuple, Optional, Any

class AgentFaction(Enum):
    SOVEREIGN_STATE = "SOVEREIGN_STATE"
    INSTITUTIONAL_CAPITAL = "INSTITUTIONAL_CAPITAL"
    PUBLIC_OPINION_BLOC = "PUBLIC_OPINION_BLOC"
    MEDIA_INFLUENCER = "MEDIA_INFLUENCER"
    REGULATORY_BODY = "REGULATORY_BODY"

@dataclass
class SwarmAgent:
    agent_id: str
    name: str
    faction: AgentFaction
    influence_weight: float
    belief_vector: List[float]  # Multi-dimensional stance [-1.0, 1.0]
    token_budget: int = 1000

@dataclass
class Coalition:
    members: Tuple[str, ...]
    value: float
    internal_synergy: float

@dataclass
class CoalitionStructureResult:
    coalitions: List[Coalition]
    total_welfare: float
    algorithm: str
    execution_time_us: float
    iterations: int = 1

@dataclass
class InfluenceResult:
    seed_agents: List[str]
    expected_reach: float
    activation_percentage: float
    algorithm: str
    execution_time_us: float

@dataclass
class ConsensusRankingResult:
    ranked_outcomes: List[str]
    total_kendall_tau_distance: float
    agreement_score: float
    algorithm: str
    execution_time_us: float

@dataclass
class BenchmarkComparison:
    problem_name: str
    optimizer_algorithm: str
    optimizer_score: float
    optimizer_latency_us: float
    evolutionary_baseline: str
    baseline_score: float
    baseline_latency_us: float
    speedup_multiplier: float
    quality_advantage_pct: float
