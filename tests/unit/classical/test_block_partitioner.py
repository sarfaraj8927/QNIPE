import logging
from pathlib import Path

import numpy as np
import pytest
from paqnipe.classical.preprocessing.block_partitioner import BlockPartitioner

_LOG = logging.getLogger(__name__)


class TestBlockPartitioner:
    """Unit tests for the BlockPartitioner class."""

    @pytest.fixture(autouse=True)
    def _setup(self) -> None:
        self.partitioner = BlockPartitioner()

    def test_partition_returns_list_of_arrays(self) -> None:
        """Test that partition returns a list of numpy arrays."""
        image = np.zeros((8, 8), dtype=np.uint8)
        blocks = self.partitioner.partition(image, 4)
        
        assert isinstance(blocks, list)
        assert len(blocks) == 4
        for block in blocks:
            assert isinstance(block, np.ndarray)
            assert block.shape == (4, 4)
        _LOG.debug("Partition returned %d blocks of shape %s", len(blocks), blocks[0].shape)

    def test_partition_odd_block_size_raises_error(self) -> None:
        """Test that partition raises error when image cannot be evenly divided."""
        image = np.zeros((5, 5), dtype=np.uint8)
        
        with pytest.raises(ValueError, match="cannot be evenly divided"):
            self.partitioner.partition(image, 3)
        _LOG.debug("Correctly raised ValueError for uneven division")

    def test_reconstruct_returns_same_shape(self) -> None:
        """Test that reconstruct returns an array with the original shape."""
        original_shape = (8, 8)
        image = np.random.randint(0, 255, original_shape, dtype=np.uint8)
        
        blocks = self.partitioner.partition(image, 4)
        reconstructed = self.partitioner.reconstruct(blocks, original_shape)
        
        assert reconstructed.shape == original_shape
        assert reconstructed.dtype == np.uint8
        _LOG.debug("Reconstructed image has shape %s", reconstructed.shape)

    def test_roundtrip_exact_recovery(self) -> None:
        """Test that partition -> reconstruct recovers the original image exactly."""
        original_image = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ], dtype=np.uint8)
        
        blocks = self.partitioner.partition(original_image, 2)
        reconstructed = self.partitioner.reconstruct(blocks, (4, 4))
        
        np.testing.assert_array_equal(original_image, reconstructed)
        _LOG.debug("Roundtrip exact recovery verified")

    def test_reconstruct_wrong_block_count_raises_error(self) -> None:
        """Test that reconstruct raises error when block count doesn't match."""
        wrong_blocks = [np.zeros((2, 2), dtype=np.uint8) for _ in range(5)]
        
        with pytest.raises(ValueError, match="Expected"):
            self.partitioner.reconstruct(wrong_blocks, (4, 4))
        _LOG.debug("Correctly raised ValueError for wrong block count")