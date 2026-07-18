"""Classical image loading interfaces for the PA-QNIPE preprocessing layer.

This module defines the repository-facing skeleton for loading cover and secret
images before later preprocessing stages such as partitioning, activity
analysis, and encoding.
"""

from __future__ import annotations

from pathlib import Path
from typing import TypeAlias


PathLike: TypeAlias = str | Path
ImageData: TypeAlias = object


class ImageLoader:
    """Skeleton interface for cover and secret image ingestion.

    The concrete implementation is expected to:

    - load cover images for grayscale preprocessing
    - load secret payload images for downstream formatting
    - normalize image intensities to the configured bit depth

    Algorithmic behavior is intentionally deferred.
    """

    def load_cover(self, path: PathLike) -> ImageData:
        """Load a cover image from disk.

        Args:
            path: Filesystem location of the cover image.

        Returns:
            A placeholder typed image object for the loaded cover image.

        Raises:
            NotImplementedError: Always raised in this skeleton.
        """

        raise NotImplementedError("ImageLoader.load_cover is not implemented.")

    def load_secret(self, path: PathLike) -> ImageData:
        """Load a secret image or payload representation from disk.

        Args:
            path: Filesystem location of the secret image or payload source.

        Returns:
            A placeholder typed image object for the loaded secret input.

        Raises:
            NotImplementedError: Always raised in this skeleton.
        """

        raise NotImplementedError("ImageLoader.load_secret is not implemented.")

    def normalize_intensity(self, image: ImageData, q: int) -> ImageData:
        """Normalize image intensity values to the configured bit depth.

        Args:
            image: Loaded image data to normalize.
            q: Target intensity bit depth.

        Returns:
            A placeholder typed image object containing normalized data.

        Raises:
            NotImplementedError: Always raised in this skeleton.
        """

        raise NotImplementedError("ImageLoader.normalize_intensity is not implemented.")
