# CI/CD Setup Guide

## GitHub Actions Workflow

This repository includes a comprehensive CI/CD pipeline using GitHub Actions. However, due to GitHub App permissions, the workflow file cannot be automatically committed.

### Setup Instructions

1. **Enable Workflow Permissions**
   - Go to your repository on GitHub
   - Navigate to: Settings → Actions → General
   - Under "Workflow permissions", select:
     - ✅ **Read and write permissions**
   - Click "Save"

2. **Add the Workflow File**

   Copy the workflow template to the correct location:

   ```bash
   mkdir -p .github/workflows
   cp .github-workflows-ci.yml.template .github/workflows/ci.yml
   git add .github/workflows/ci.yml
   git commit -m "ci: add GitHub Actions workflow"
   git push
   ```

3. **Verify the Workflow**
   - Go to the "Actions" tab on GitHub
   - You should see the CI workflow running
   - The workflow will run on every push and pull request

## What the CI/CD Pipeline Does

### 🔍 Code Quality Checks
- Lints code with Ruff
- Checks formatting with Black
- Validates code style and best practices

### 🔒 Security Scanning
- Runs Bandit for security vulnerabilities
- Checks dependencies with Safety
- Scans for common security issues

### 🎯 Type Checking
- Static type analysis with MyPy
- Ensures type safety across the codebase

### 🧪 Testing Matrix
Tests run on multiple configurations:
- **Python versions**: 3.9, 3.10, 3.11, 3.12
- **Operating systems**: Ubuntu, Windows, macOS
- **Coverage reporting**: Uploads to Codecov

### 📦 Build & Distribution
- Builds the package with Hatch
- Validates the distribution
- Checks package metadata

### 📚 Documentation
- Builds documentation
- Validates markdown files

### ✅ Pre-commit Hooks
- Runs all pre-commit hooks
- Ensures code quality before merge

## Alternative: Local CI/CD

If you prefer not to use GitHub Actions, you can run all checks locally:

```bash
# Run all quality checks
make check-all

# Or run individually
make lint          # Lint with Ruff
make format        # Format with Black
make type-check    # Type check with MyPy
make test-cov      # Run tests with coverage
make pre-commit    # Run all pre-commit hooks
```

## Continuous Integration Best Practices

1. **Always run tests locally before pushing**
   ```bash
   make test-cov
   ```

2. **Run pre-commit hooks before committing**
   ```bash
   make pre-commit
   ```

3. **Check the CI status before merging PRs**
   - All checks must pass
   - Code coverage should not decrease

4. **Keep dependencies up to date**
   ```bash
   pre-commit autoupdate
   ```

## Troubleshooting

### Workflow not running?
- Check repository permissions (Settings → Actions)
- Ensure workflow file is in `.github/workflows/`
- Check for syntax errors in the YAML file

### Tests failing in CI but passing locally?
- Check Python version compatibility
- Verify environment variables
- Review dependency versions

### Permission errors?
- Enable "Read and write permissions" in Actions settings
- Check branch protection rules

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Hatch Documentation](https://hatch.pypa.io/)
- [Pre-commit Documentation](https://pre-commit.com/)

## Need Help?

If you encounter issues:
1. Check the Actions logs on GitHub
2. Review the [DEVELOPMENT.md](DEVELOPMENT.md) guide
3. Open an issue on GitHub
