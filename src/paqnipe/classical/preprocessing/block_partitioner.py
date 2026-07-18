"""Block partitioning interfaces for the PA-QNIPE preprocessing layer.

This module defines the repository-facing skeleton for splitting an image into
non-overlapping blocks and reconstructing a full image from block data.
"""

from __future__ import annotations

from typing import TypeAlias


ImageData: TypeAlias = object
BlockCollection: TypeAlias = object
ImageShape: TypeAlias = tuple[int, int]


class BlockPartitioner:
    """Skeleton interface for block-based image partitioning.

    The concrete implementation is expected to:

    - split an image into non-overlapping spatial blocks
    - preserve enough structure for later reconstruction
    - rebuild a full image from block collections

    Algorithmic behavior is intentionally deferred.
    """

    def partition(self, image: ImageData, block_size: int) -> BlockCollection:
        """Partition an image into non-overlapping blocks.

        Args:
            image: Image data to partition.
            block_size: Edge length of each square block.

        Returns:
            A placeholder typed collection of blocks.

        Raises:
            NotImplementedError: Always raised in this skeleton.
        """

        raise NotImplementedError("BlockPartitioner.partition is not implemented.")

    def reconstruct(self, blocks: BlockCollection, shape: ImageShape) -> ImageData:
        """Reconstruct an image from a collection of blocks.

        Args:
            blocks: Block collection produced by the partitioning step.
            shape: Target image shape for the reconstructed output.

        Returns:
            A placeholder typed image object for the reconstructed image.

        Raises:
            NotImplementedError: Always raised in this skeleton.
        """

        raise NotImplementedError("BlockPartitioner.reconstruct is not implemented.")
