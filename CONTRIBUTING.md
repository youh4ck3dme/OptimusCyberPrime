# 🛠 Contributing to iOS Security Analyzer

Thank you for considering contributing to **iOS Security Analyzer**.

## 📌 Development Workflow
1. Fork the repository.
2. Create a feature/fix branch.
3. Make focused changes with clear commit messages.
4. Run local checks.
5. Open a pull request with a concise summary.

## 🌿 Branch Naming
Use descriptive names, for example:
- `feature/add-json-report`
- `fix/ip-resolution-fallback`
- `docs/update-installation-guide`

## ✅ Local Checks
Run before opening a PR:
```sh
python3 -m py_compile ios_security_analyzer.py
```

Optional runtime smoke test:
```sh
python3 ios_security_analyzer.py
```

## 🧹 Code Style
- Keep functions small and explicit.
- Prefer defensive error handling in environment-dependent probes.
- Avoid breaking report format compatibility.

## 📝 Commit Guidelines
- Use imperative mood in subject line, e.g. `Add report sanitization helper`.
- Keep subject line short and specific.
- Include a short body when context is helpful.

## 🔍 Pull Request Checklist
- [ ] Documentation updated (if behavior changed)
- [ ] Script compiles/runs locally
- [ ] Error handling considered for constrained environments
- [ ] Report output remains readable and stable
