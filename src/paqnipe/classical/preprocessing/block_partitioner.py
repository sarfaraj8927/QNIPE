"""Block partitioning interfaces for the PA-QNIPE preprocessing layer.

This module defines the repository-facing skeleton for splitting an image into
non-overlapping blocks and reconstructing a full image from block data.
"""

from __future__ import annotations

import logging
from typing import TypeAlias

import numpy as np
from numpy.typing import NDArray

PathLike: TypeAlias = str | object  # Placeholder, not used in this module

ImageData: TypeAlias = NDArray[np.uint8]
BlockCollection: TypeAlias = list[NDArray[np.uint8]]
ImageShape: TypeAlias = tuple[int, int]

_LOG = logging.getLogger(__name__)


class BlockPartitioner:
    """Splits images into non-overlapping blocks and reconstructs them."""

    def partition(self, image: ImageData, block_size: int) -> BlockCollection:
        """Partition an image into non-overlapping blocks.

        Args:
            image: Image data to partition (2D numpy array).
            block_size: Edge length of each square block.

        Returns:
            A list of 2D numpy arrays, each representing a block.

        Raises:
            ValueError: If the image cannot be evenly divided by block_size.
        """
        _LOG.info("Partitioning image with shape %s into blocks of size %d", image.shape, block_size)
        
        height, width = image.shape
        if height % block_size != 0 or width % block_size != 0:
            raise ValueError(
                f"Image size {image.shape} cannot be evenly divided by block size {block_size}"
            )
        
        blocks = []
        for i in range(0, height, block_size):
            for j in range(0, width, block_size):
                block = image[i:i + block_size, j:j + block_size]
                blocks.append(block)
        
        _LOG.debug("Created %d blocks from image", len(blocks))
        return blocks

    def reconstruct(self, blocks: BlockCollection, shape: ImageShape) -> ImageData:
        """Reconstruct an image from a collection of blocks.

        Args:
            blocks: List of block arrays produced by the partitioning step.
            shape: Target image shape for the reconstructed output.

        Returns:
            Reconstructed 2D numpy array.

        Raises:
            ValueError: If the number of blocks doesn't match the expected count.
        """
        _LOG.info("Reconstructing image of shape %s from %d blocks", shape, len(blocks))
        
        height, width = shape
        block_h = blocks[0].shape[0] if blocks else 0
        block_w = blocks[0].shape[1] if blocks else 0
        
        expected_blocks = (height // block_h) * (width // block_w) if block_h > 0 and block_w > 0 else 0
        if len(blocks) != expected_blocks:
            raise ValueError(
                f"Expected {expected_blocks} blocks for shape {shape}, got {len(blocks)}"
            )
        
        reconstructed = np.zeros(shape, dtype=np.uint8)
        block_idx = 0
        
        for i in range(0, height, block_h):
            for j in range(0, width, block_w):
                reconstructed[i:i + block_h, j:j + block_w] = blocks[block_idx]
                block_idx += 1
        
        _LOG.debug("Image reconstruction complete")
        return reconstructed