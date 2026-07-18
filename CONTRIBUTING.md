# Contributing

Thank you for contributing to PA-QNIPE.

This repository is currently at Phase 1 of the architecture roadmap, so contributions should stay
within repository infrastructure unless the maintainers explicitly open later phases.

## Ground Rules

1. Keep changes aligned with `QNIP_system_architecture.pdf`.
2. Preserve the module layout and naming defined by the architecture.
3. Do not add algorithmic implementations to placeholder modules during infrastructure-only work.
4. Keep formatting, linting, typing, and tests green before requesting review.

## Local Setup

```bash
python -m pip install -r requirements.txt
pre-commit install
```

## Quality Checks

Run these before opening a pull request:

```bash
ruff check .
black --check .
mypy src
pytest
```

## Pull Requests

Each pull request should include:

- a short summary of the architectural area touched
- any changes to repository structure or tooling
- any follow-up work left intentionally out of scope
