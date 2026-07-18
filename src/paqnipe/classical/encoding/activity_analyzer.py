"""Activity analysis interfaces for the PA-QNIPE classical encoding layer.

This module defines the architecture-specified surface for computing Laplacian-
based local activity maps used by the adaptive encoding pipeline.
"""

from __future__ import annotations

import logging
from typing import TypeAlias


logger = logging.getLogger(__name__)

ImageData: TypeAlias = object
ActivityMap: TypeAlias = object


class ActivityAnalyzerError(Exception):
    """Placeholder exception for activity-analysis failures."""


class ActivityAnalyzer:
    """Skeleton interface for local-activity analysis.

    The concrete implementation is expected to:

    - compute Laplacian responses over image data
    - derive local activity estimates from those responses
    - normalize activity values for downstream adaptive quantization

    Algorithmic behavior is intentionally deferred.
    """

    def compute_laplacian(self, image: ImageData) -> ActivityMap:
        """Compute the Laplacian response for an input image.

        Args:
            image: Image data to analyze.

        Returns:
            A placeholder typed object representing Laplacian output.

        Raises:
            ActivityAnalyzerError: Placeholder for domain-specific failures.
            NotImplementedError: Always raised in this skeleton.
        """

        logger.debug("compute_laplacian called for image type %s", type(image).__name__)
        raise NotImplementedError("ActivityAnalyzer.compute_laplacian is not implemented.")

    def local_activity_map(self, image: ImageData, window_size: int) -> ActivityMap:
        """Compute a local activity map from an input image.

        Args:
            image: Image data to analyze.
            window_size: Neighborhood size used for local activity estimation.

        Returns:
            A placeholder typed object representing the local activity map.

        Raises:
            ActivityAnalyzerError: Placeholder for domain-specific failures.
            NotImplementedError: Always raised in this skeleton.
        """

        logger.debug(
            "local_activity_map called for image type %s with window_size=%d",
            type(image).__name__,
            window_size,
        )
        raise NotImplementedError("ActivityAnalyzer.local_activity_map is not implemented.")

    def normalize_activity(self, activity_map: ActivityMap) -> ActivityMap:
        """Normalize activity values for downstream capacity allocation.

        Args:
            activity_map: Activity map produced by a prior analysis step.

        Returns:
            A placeholder typed object representing normalized activity data.

        Raises:
            ActivityAnalyzerError: Placeholder for domain-specific failures.
            NotImplementedError: Always raised in this skeleton.
        """

        logger.debug(
            "normalize_activity called for activity_map type %s",
            type(activity_map).__name__,
        )
        raise NotImplementedError("ActivityAnalyzer.normalize_activity is not implemented.")
