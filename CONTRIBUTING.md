# Contributing to iOS Security Analyzer

Thanks for your interest in contributing. This guide defines the standard branch, commit, testing, and pull request workflow for this repository.

## Contribution Standards

Please follow these standards for every change:

- Keep changes scoped to a single purpose per pull request.
- Prefer small, reviewable commits.
- Maintain or improve readability.
- Do not introduce unrelated refactors in feature/fix PRs.
- Update documentation (`README.md`, this file, inline comments) when behavior changes.
- Ensure commands in docs are copy/paste runnable.

## Branch Workflow

1. Fork the repository (if contributing externally).
2. Sync your local `main` branch.
3. Create a feature branch from `main`.

```bash
git checkout main
git pull origin main
git checkout -b feature/<short-description>
```

Branch naming conventions:

- `feature/<short-description>` for new features.
- `fix/<short-description>` for bug fixes.
- `docs/<short-description>` for documentation-only updates.
- `chore/<short-description>` for maintenance.

## Commit Workflow

Make focused commits and use clear, imperative commit messages.

```bash
git add <files>
git commit -m "docs: improve README and contribution workflow"
```

Recommended commit style:

- `feat: ...`
- `fix: ...`
- `docs: ...`
- `refactor: ...`
- `test: ...`
- `chore: ...`

Before pushing, optionally squash or reword noisy commits.

## Lint / Test Commands

Run these before opening a PR.

### Required baseline checks

```bash
python3 -m py_compile ios_security_analyzer.py
```

### Optional local checks (if tools are installed)

```bash
python3 -m pip install ruff black
ruff check .
black --check .
```

If optional tools are unavailable in your environment, mention that in the PR description.

## Pull Request (PR) Workflow

1. Push your branch.
2. Open a pull request against `main`.
3. Fill in a clear PR description.
4. Address review comments with follow-up commits (or squash when requested).

```bash
git push -u origin feature/<short-description>
```

PR checklist:

- [ ] Change is scoped and documented.
- [ ] Baseline checks pass locally.
- [ ] README/CONTRIBUTING updated if behavior or workflow changed.
- [ ] No sensitive data or secrets included.

## PR Description Template

Use this structure when opening a PR:

```markdown
## Summary
- What changed
- Why it changed

## Validation
- Commands run
- Results

## Notes
- Limitations, follow-ups, or environment constraints
```

## Reporting Issues

When filing an issue, include:

- Expected behavior.
- Actual behavior.
- Reproduction steps.
- Environment details (OS, Python version, shell/container details).
- Relevant logs or screenshots.

## Code of Conduct

Be respectful and constructive in all discussions and reviews.
