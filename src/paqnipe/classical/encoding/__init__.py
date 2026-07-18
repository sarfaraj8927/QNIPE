"""Classical encoding interfaces for the PA-QNIPE architecture.

This package contains the non-algorithmic skeletons for the classical encoding
modules defined in the architecture specification.
"""

from .activity_analyzer import ActivityAnalyzer, ActivityAnalyzerError
from .adaptive_quantizer import AdaptiveQuantizer, AdaptiveQuantizerError
from .normalization_engine import NormalizationEngine, NormalizationEngineError
from .phase_encoder import PhaseEncoder, PhaseEncoderError
from .secret_formatter import SecretFormatter, SecretFormatterError

__all__ = [
    "ActivityAnalyzer",
    "ActivityAnalyzerError",
    "AdaptiveQuantizer",
    "AdaptiveQuantizerError",
    "NormalizationEngine",
    "NormalizationEngineError",
    "PhaseEncoder",
    "PhaseEncoderError",
    "SecretFormatter",
    "SecretFormatterError",
]
