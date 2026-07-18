# PA-QNIPE

Phase 1 infrastructure package for PA-QNIPE (Perceptually Adaptive Quantum Image Steganography),
aligned to the architecture specification dated July 18, 2026.

This repository currently contains:

- the infrastructure package under `src/paqnipe/utils/`
- minimal Phase 1 support for configuration loading and experiment logging
- repository automation for linting, typing, and CI

No algorithmic modules are implemented.

## Scope

The scaffold is based on:

- `A_QNIPE.pdf`
- `QNIP_system_architecture.pdf`

The implementation roadmap in the architecture defines Phase 1 as:

1. initialize the repository scaffold
2. add CI/CD and pre-commit hooks
3. implement `PAQNIPEConfig`
4. implement `ExperimentLogger`

This repository state now reflects only that infrastructure scope.

## Repository Layout

```text
pa-qnipe/
├── configs/
│   ├── default.yaml
│   ├── high_capacity.yaml
│   └── nisq_4096.yaml
├── src/
│   └── paqnipe/
│       ├── utils/
│       │   ├── config_manager.py
│       │   ├── logger.py
│       │   └── __init__.py
├── tests/
│   ├── unit/
│   │   ├── test_config_manager.py
│   │   └── test_logger.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .pre-commit-config.yaml
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── PROJECT_STATUS.md
├── TODO.md
├── pyproject.toml
├── requirements.txt
└── setup.py
```

## Infrastructure Package

- `config_manager.py`: `PAQNIPEConfig` YAML-backed configuration model
- `logger.py`: `ExperimentLogger` for structured experiment logging
- `__init__.py`: package exports for the infrastructure layer

## Configuration Profiles

- `configs/default.yaml`: balanced placeholder profile
- `configs/nisq_4096.yaml`: placeholder profile aligned to the paper's NISQ-style `M2 = 4096`
  extraction constraint
- `configs/high_capacity.yaml`: placeholder profile for a higher-capacity phase-resolution regime

## Development

```bash
python -m pip install -r requirements.txt
pre-commit install
pytest tests/unit
```

## Current Status

See [PROJECT_STATUS.md](PROJECT_STATUS.md) and [TODO.md](TODO.md) for the roadmap checkpoint and
follow-on work.
