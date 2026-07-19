import logging
from pathlib import Path

import numpy as np
import pytest
from paqnipe.classical.preprocessing.image_loader import ImageLoader

_LOG = logging.getLogger(__name__)


class TestImageLoader:
    """Unit tests for the ImageLoader class."""

    @pytest.fixture(autouse=True)
    def _setup(self) -> None:
        self.loader = ImageLoader()
        self.dummy_path = Path("dummy_image.png")

    def test_load_cover_returns_numpy_array(self) -> None:
        """Test that load_cover returns a numpy array with expected shape and dtype."""
        image = self.loader.load_cover(self.dummy_path)
        assert isinstance(image, np.ndarray)
        assert image.shape == (256, 256)
        assert image.dtype == np.uint8
        _LOG.debug("load_cover returned a numpy array with shape %s and dtype %s", image.shape, image.dtype)

    def test_load_secret_returns_numpy_array(self) -> None:
        """Test that load_secret returns a numpy array with expected shape and dtype."""
        secret = self.loader.load_secret(self.dummy_path)
        assert isinstance(secret, np.ndarray)
        assert secret.shape == (256, 256)
        assert secret.dtype == np.uint8
        _LOG.debug("load_secret returned a numpy array with shape %s and dtype %s", secret.shape, secret.dtype)

    @pytest.mark.parametrize("q_bits, expected_max_val", [
        (1, 1),
        (2, 3),
        (8, 255),
    ])
    def test_normalize_intensity(self, q_bits: int, expected_max_val: int) -> None:
        """Test normalization of image intensity to a specified bit depth."""
        # Create a dummy image with varying intensity values
        original_image = np.array([[0, 100, 200, 255]], dtype=np.uint8)
        normalized_image = self.loader.normalize_intensity(original_image, q_bits)

        assert isinstance(normalized_image, np.ndarray)
        assert normalized_image.dtype == np.uint8
        assert np.max(normalized_image) <= expected_max_val
        assert np.min(normalized_image) >= 0
        _LOG.debug(
            "Normalized image to %d bits. Original max: %d, Normalized max: %d",
            q_bits, np.max(original_image), np.max(normalized_image)
        )

    def test_normalize_intensity_with_zero_max(self) -> None:
        """Test normalization when the input image has a max value of 0."""
        original_image = np.array([[0, 0], [0, 0]], dtype=np.uint8)
        normalized_image = self.loader.normalize_intensity(original_image, 8)
        assert np.all(normalized_image == 0)
        _LOG.debug("Normalized image with zero max value: %s", normalized_image)