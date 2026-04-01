# Contributing

Thanks for contributing.

## Expectations

- Keep pull requests narrow and intentional.
- Prefer simple, explicit implementations over clever ones.
- Document behavior changes in the same pull request.
- Run the fastest relevant checks before opening or updating a pull request.
- Keep unrelated cleanup out of scope.

## Local workflow

At minimum, contributors should run the fastest checks available for the area they changed.

Examples:

- formatter checks
- linter checks
- type checks
- focused tests
- `git diff --check` for docs and text-heavy changes

If the repository later adds project-specific commands, document them here and in the README.

## Pull request rules

- Use Conventional Commit-style titles such as `feat:`, `fix:`, `docs:`, `ci:`, or `chore:`.
- Link the canonical issue or related pull request in the PR template.
- Fill out the pull request checklist completely.
- Explain tradeoffs or follow-up work in the PR body when relevant.
- Expect an automatically requested reviewer once the pull request is ready for review.

## Issue and PR intake

- Search existing issues and pull requests before opening a new one.
- Pick the closest matching `Area` in the issue form so automation can route triage correctly.
- New issues are assigned automatically from the checked-in maintainer rotation.
- Maintainers can close duplicates with `/duplicate #123`.
- Maintainers can close superseded pull requests with `/superseded-by #123`.

## Communication

- Bug reports, feature requests, and project tasks should use the checked-in issue forms.
- Security issues should follow [SECURITY.md](SECURITY.md).
- Significant project direction changes should be reflected in [docs/vision.md](docs/vision.md) or [docs/roadmap.md](docs/roadmap.md).
