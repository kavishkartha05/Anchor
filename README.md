# PROJECT_NAME

PROJECT_DESCRIPTION

This repository was started from the Codelab open-source template and is intended to ship with a clean, GitHub-native foundation:

- clear contributor and maintainer documentation
- issue and pull request intake that reduces low-signal churn
- deterministic issue assignment and PR reviewer routing
- label automation and lightweight repository hygiene
- security and governance defaults that are explicit without being heavy

## Getting started

1. Replace `PROJECT_NAME` and `PROJECT_DESCRIPTION` in this file.
2. Replace `SECURITY_CONTACT_EMAIL` in [SECURITY.md](SECURITY.md) and [.github/ISSUE_TEMPLATE/config.yml](.github/ISSUE_TEMPLATE/config.yml).
3. Replace placeholder maintainer handles in [.github/CODEOWNERS](.github/CODEOWNERS) and [.github/maintainers.yml](.github/maintainers.yml).
4. Update [docs/vision.md](docs/vision.md) and [docs/roadmap.md](docs/roadmap.md) for the project.
5. Extend [.github/dependabot.yml](.github/dependabot.yml) for the package ecosystems used by the project.
6. Enable the repository settings listed in [docs/maintainers.md](docs/maintainers.md).

## What this repository includes

- `README.md`: starter overview and setup guidance
- `CONTRIBUTING.md`: contribution rules and local workflow expectations
- `CODE_OF_CONDUCT.md`: participation standards
- `SECURITY.md`: private disclosure path for vulnerabilities
- `GOVERNANCE.md`: maintainer and decision-making model
- `docs/`: maintainer-facing setup notes plus lightweight vision and roadmap docs
- `.github/`: issue forms, PR template, labels, maintainer routing config, Dependabot, and GitHub Actions workflows

## Recommended repository layout

This template is intentionally language-agnostic. Pick a layout that fits the project and keep it consistent.

- `src/`, `app/`, `apps/`, `packages/`, or `crates/` for code
- `tests/` for automated tests when the ecosystem uses a dedicated test directory
- `docs/` for roadmap, architecture, maintainer notes, and project decisions
- `.github/` for repository automation and collaboration rules

## Local documentation checks

When editing repository docs or GitHub metadata, these are the first checks to run:

```bash
git diff --check
```

The checked-in GitHub Actions workflows also validate Markdown and links on pull requests and pushes to `main`.

## Customization checklist

Before calling a new repository ready, update:

- project name, summary, and status
- `SECURITY_CONTACT_EMAIL`
- maintainer list in `.github/CODEOWNERS`
- maintainer routing in `.github/maintainers.yml`
- package ecosystems in `.github/dependabot.yml`
- label taxonomy in `.github/labels.json` if the project needs different categories
- area mappings in `.github/labeler.yml`
- any product-specific docs, commands, or release process details

## Template principles

- small diffs
- explicit project policies
- fast contributor onboarding
- GitHub-native automation before custom infrastructure
- language and framework neutrality until the project needs more
