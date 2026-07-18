"""Experiment logging infrastructure for the PA-QNIPE scaffold."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Mapping

from .config_manager import PAQNIPEConfig


class ExperimentLogger:
    """Minimal file-backed logger for architecture-defined experiment tracking."""

    def __init__(
        self,
        name: str = "paqnipe",
        log_dir: str | Path = "logs",
        level: int = logging.INFO,
    ) -> None:
        self.name = name
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_path = self.log_dir / f"{name}.log"

        self._logger = logging.getLogger(f"paqnipe.{name}")
        self._logger.setLevel(level)
        self._logger.propagate = False

        if not self._logger.handlers:
            formatter = logging.Formatter(
                fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )

            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)

            file_handler = logging.FileHandler(self.log_path, encoding="utf-8")
            file_handler.setFormatter(formatter)

            self._logger.addHandler(stream_handler)
            self._logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        """Expose the configured logger."""

        return self._logger

    def log_phase_banner(self, phase_name: str) -> None:
        """Mark a roadmap phase boundary in the log."""

        self._logger.info("=== %s ===", phase_name)

    def log_hyperparameters(self, payload: PAQNIPEConfig | Mapping[str, Any]) -> None:
        """Write configuration details in a structured, stable format."""

        if isinstance(payload, PAQNIPEConfig):
            serializable = payload.to_dict()
        else:
            serializable = dict(payload)

        self._logger.info("hyperparameters=%s", json.dumps(serializable, sort_keys=True))
