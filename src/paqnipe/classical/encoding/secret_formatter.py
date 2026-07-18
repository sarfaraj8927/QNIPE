"""Secret-formatting interfaces for the PA-QNIPE classical encoding layer.

This module defines the architecture-specified surface for payload allocation
and bit-to-symbol conversion driven by adaptive phase resolution.
"""

from __future__ import annotations

import logging
from typing import TypeAlias


logger = logging.getLogger(__name__)

BitSequence: TypeAlias = object
PhaseResolutionMap: TypeAlias = object
SymbolData: TypeAlias = object


class SecretFormatterError(Exception):
    """Placeholder exception for secret-formatting failures."""


class SecretFormatter:
    """Skeleton interface for secret-payload allocation and formatting.

    The concrete implementation is expected to:

    - allocate payload bits to image positions using adaptive resolution
    - convert bit sequences into symbol representations
    - convert symbol representations back into bit sequences

    Algorithmic behavior is intentionally deferred.
    """

    def allocate_payload(
        self,
        bits: BitSequence,
        phase_resolution: PhaseResolutionMap,
        pixel_count: int,
    ) -> SymbolData:
        """Allocate payload data using a phase-resolution map.

        Args:
            bits: Input payload bit sequence.
            phase_resolution: Per-pixel phase-resolution assignment.
            pixel_count: Total number of pixels or positions available for allocation.

        Returns:
            A placeholder typed object representing allocated payload symbols.

        Raises:
            SecretFormatterError: Placeholder for domain-specific failures.
            NotImplementedError: Always raised in this skeleton.
        """

        logger.debug(
            "allocate_payload called for bits type %s, phase_resolution type %s, pixel_count=%d",
            type(bits).__name__,
            type(phase_resolution).__name__,
            pixel_count,
        )
        raise NotImplementedError("SecretFormatter.allocate_payload is not implemented.")

    def bits_to_symbols(self, bits: BitSequence, p: int) -> SymbolData:
        """Convert payload bits into symbols at a given phase resolution.

        Args:
            bits: Input payload bit sequence.
            p: Bit depth or phase-resolution parameter for symbolization.

        Returns:
            A placeholder typed object representing formatted symbols.

        Raises:
            SecretFormatterError: Placeholder for domain-specific failures.
            NotImplementedError: Always raised in this skeleton.
        """

        logger.debug("bits_to_symbols called for bits type %s with p=%d", type(bits).__name__, p)
        raise NotImplementedError("SecretFormatter.bits_to_symbols is not implemented.")

    def symbols_to_bits(self, symbols: SymbolData, p: int) -> BitSequence:
        """Convert symbols back into a payload bit sequence.

        Args:
            symbols: Symbol representation to decode.
            p: Bit depth or phase-resolution parameter used for symbolization.

        Returns:
            A placeholder typed object representing the recovered bit sequence.

        Raises:
            SecretFormatterError: Placeholder for domain-specific failures.
            NotImplementedError: Always raised in this skeleton.
        """

        logger.debug(
            "symbols_to_bits called for symbols type %s with p=%d",
            type(symbols).__name__,
            p,
        )
        raise NotImplementedError("SecretFormatter.symbols_to_bits is not implemented.")
