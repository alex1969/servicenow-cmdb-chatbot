## `CONTRIBUTING.md`

```markdown
# Contributing to ServiceNow CMDB Chatbot

Thank you for your interest in contributing. This project enables natural language querying of ServiceNow CMDB using a tool-enabled, memory-aware chatbot. Contributions help improve usability, reliability, and extensibility.

---

## Contribution Guidelines

### Code of Conduct
By participating, you agree to uphold a respectful, inclusive, and professional environment. Treat all contributors with courtesy.

### How to Contribute
- Report issues using GitHub Issues to document bugs, request features, or suggest improvements.
- Submit pull requests by forking the repo, creating a feature branch, and opening a PR with a clear description.
- Improve documentation by updating README, architecture docs, or notebooks.
- Add tests to ensure new features are reliable and maintainable.

### Development Workflow
1. Fork the repository
2. Clone your fork locally
3. Create a new branch:
   ```bash
   git checkout -b feature/my-feature
   ```
4. Make changes and commit:
   ```bash
   git commit -m "Add feature: my-feature"
   ```
5. Push to your fork:
   ```bash
   git push origin feature/my-feature
   ```
6. Open a Pull Request against `main`

---

## Coding Standards
- Python 3.10 or higher recommended
- Follow [PEP8](https://peps.python.org/pep-0008/) style guidelines
- Keep functions modular and well-documented
- Use descriptive commit messages
- Include docstrings for public functions and classes

---

## Secrets and Security
- Do not commit credentials (ServiceNow, OpenAI, etc.)
- Use `.env` files locally and add `.env` to `.gitignore`
- For CI/CD, configure secrets via GitHub Actions → Settings → Secrets

---

## Testing
- Place tests in the `tests/` directory
- Use `pytest` for unit testing
- Run tests locally before submitting pull requests:
  ```bash
  pytest
  ```

---

## Pull Request Checklist
- Code follows style guidelines
- Documentation updated (README, architecture, notebooks)
- Tests added or updated
- All tests pass locally
- No secrets or sensitive data committed

---

## Recognition
Contributors will be credited in the project’s release notes and documentation. Your efforts help make CMDB data accessible to everyone through conversational AI.
```

---