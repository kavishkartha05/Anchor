# Governance

## Project model

This repository starts with a maintainer-led open-source model under Codelab. The initial goal is speed with clear technical direction, not a heavyweight governance process.

## Decision making

- Maintainers set roadmap direction and merge policy.
- Contributors are encouraged to challenge designs and implementation details with concrete reasoning.
- Significant behavior or architecture changes should be reflected in the docs before or with implementation.

## Maintainers

Initial maintainership is held by the repository owners in `CODEOWNERS`, and automation routing is configured in `.github/maintainers.yml`. Additional maintainers may be added when they demonstrate sustained technical judgment, review quality, and stewardship of the project.

## Review standards

- New public interfaces should be reviewed for long-term maintainability.
- Project-specific implementation details should not leak across package or application boundaries without a clear interface.
- Automation and docs changes are treated as product surface area and reviewed accordingly.

## Evolution

This governance model is intentionally light. If the contributor base grows, the project can add maintainership tiers, RFCs, or more formal decision processes later.
