"""Adaptive quantization interfaces for the PA-QNIPE classical encoding layer.

This module defines the architecture-specified surface for perceptually adaptive
phase-resolution assignment and aggregate capacity accounting.
"""

from __future__ import annotations

import logging
from typing import TypeAlias


logger = logging.getLogger(__name__)

ActivityMap: TypeAlias = object
PhaseResolutionMap: TypeAlias = object


class AdaptiveQuantizerError(Exception):
    """Placeholder exception for adaptive-quantization failures."""


class AdaptiveQuantizer:
    """Skeleton interface for perceptually adaptive quantization.

    The concrete implementation is expected to:

    - assign per-pixel phase resolution from image activity
    - aggregate payload capacity from the assigned phase-resolution map
    - validate adaptive-capacity behavior against reference baselines

    Algorithmic behavior is intentionally deferred.
    """

    def compute_phase_resolution(
        self,
        activity_map: ActivityMap,
        p_min: int,
        p_max: int,
    ) -> PhaseResolutionMap:
        """Compute a phase-resolution map from activity statistics.

        Args:
            activity_map: Activity map used for adaptive resolution assignment.
            p_min: Minimum permitted phase resolution.
            p_max: Maximum permitted phase resolution.

        Returns:
            A placeholder typed object representing per-pixel phase resolution.

        Raises:
            AdaptiveQuantizerError: Placeholder for domain-specific failures.
            NotImplementedError: Always raised in this skeleton.
        """

        logger.debug(
            "compute_phase_resolution called with p_min=%d, p_max=%d, activity_map type=%s",
            p_min,
            p_max,
            type(activity_map).__name__,
        )
        raise NotImplementedError("AdaptiveQuantizer.compute_phase_resolution is not implemented.")

    def aggregate_capacity(self, phase_resolution: PhaseResolutionMap) -> int:
        """Aggregate payload capacity from a phase-resolution map.

        Args:
            phase_resolution: Per-pixel phase-resolution assignment.

        Returns:
            A placeholder integer for aggregate payload capacity.

        Raises:
            AdaptiveQuantizerError: Placeholder for domain-specific failures.
            NotImplementedError: Always raised in this skeleton.
        """

        logger.debug(
            "aggregate_capacity called for phase_resolution type %s",
            type(phase_resolution).__name__,
        )
        raise NotImplementedError("AdaptiveQuantizer.aggregate_capacity is not implemented.")

    def validate_capacity_gain(
        self,
        adaptive_capacity: int,
        uniform_capacity: int,
    ) -> bool:
        """Validate adaptive-capacity behavior against a reference baseline.

        Args:
            adaptive_capacity: Capacity derived from adaptive quantization.
            uniform_capacity: Capacity derived from a uniform allocation baseline.

        Returns:
            A placeholder boolean indicating whether the validation passed.

        Raises:
            AdaptiveQuantizerError: Placeholder for domain-specific failures.
            NotImplementedError: Always raised in this skeleton.
        """

        logger.debug(
            "validate_capacity_gain called with adaptive_capacity=%d, uniform_capacity=%d",
            adaptive_capacity,
            uniform_capacity,
        )
        raise NotImplementedError("AdaptiveQuantizer.validate_capacity_gain is not implemented.")
