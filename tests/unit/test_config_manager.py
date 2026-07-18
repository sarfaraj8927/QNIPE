from __future__ import annotations

from pathlib import Path

from paqnipe.utils import PAQNIPEConfig


def test_load_default_config() -> None:
    config = PAQNIPEConfig.load_from_yaml(Path("configs/default.yaml"))

    assert config.profile_name == "default"
    assert config.n == 3
    assert config.M1 == 8192
    assert config.M2 == 4096
    assert config.noise_params["depolarizing_probability"] == 0.0
