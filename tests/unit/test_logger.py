from __future__ import annotations

from pathlib import Path

from paqnipe.utils import ExperimentLogger, PAQNIPEConfig


def test_experiment_logger_writes_hyperparameters(tmp_path: Path) -> None:
    logger = ExperimentLogger(name="unit_test_logger", log_dir=tmp_path / "logs")
    config = PAQNIPEConfig.load_from_yaml(Path("configs/default.yaml"))

    logger.log_phase_banner("Phase 1 test")
    logger.log_hyperparameters(config)

    for handler in logger.get_logger().handlers:
        handler.flush()

    contents = (tmp_path / "logs" / "unit_test_logger.log").read_text(encoding="utf-8")
    assert "Phase 1 test" in contents
    assert '"profile_name": "default"' in contents
