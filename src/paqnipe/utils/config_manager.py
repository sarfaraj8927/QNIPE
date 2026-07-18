"""Configuration infrastructure for the PA-QNIPE scaffold."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass(slots=True)
class PAQNIPEConfig:
    """Container for architecture-defined configuration fields."""

    n: int
    q: int
    p_min: int
    p_max: int
    B: int
    M: int
    M1: int
    M2: int
    epsilon: float
    noise_params: dict[str, Any] = field(default_factory=dict)
    profile_name: str = "default"
    description: str = ""
    seed: int | None = None

    @classmethod
    def load_from_yaml(cls, path: str | Path) -> "PAQNIPEConfig":
        """Load a Phase 1 configuration from a YAML file."""

        config_path = Path(path)
        data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        return cls(
            n=int(data["n"]),
            q=int(data["q"]),
            p_min=int(data["p_min"]),
            p_max=int(data["p_max"]),
            B=int(data["B"]),
            M=int(data["M"]),
            M1=int(data["M1"]),
            M2=int(data["M2"]),
            epsilon=float(data["epsilon"]),
            noise_params=dict(data.get("noise_params", {})),
            profile_name=str(data.get("profile_name", config_path.stem)),
            description=str(data.get("description", "")),
            seed=int(data["seed"]) if data.get("seed") is not None else None,
        )

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation for logging and tooling."""

        return {
            "profile_name": self.profile_name,
            "description": self.description,
            "n": self.n,
            "q": self.q,
            "p_min": self.p_min,
            "p_max": self.p_max,
            "B": self.B,
            "M": self.M,
            "M1": self.M1,
            "M2": self.M2,
            "epsilon": self.epsilon,
            "noise_params": self.noise_params,
            "seed": self.seed,
        }
