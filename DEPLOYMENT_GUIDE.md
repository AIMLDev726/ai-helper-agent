# 🚀 Deployment Guide for PyPI

Your AI Helper Agent package is now properly structured for PyPI deployment! Here's how to deploy it:

## 📋 Pre-deployment Checklist

✅ **Proper directory structure** - Complete  
✅ **pyproject.toml configured** - Complete  
✅ **README.md with examples** - Complete  
✅ **LICENSE file** - Complete  
✅ **Test suite** - Complete  
✅ **MANIFEST.in** - Complete  
✅ **Changelog** - Complete  

## 🛠️ Before Deploying

### 1. Update Package Information
Edit the following in `pyproject.toml`:
- Change `"Your Name"` and `"your.email@example.com"` to your actual details
- Update the GitHub URLs to your repository
- Verify the version number

### 2. Set Up PyPI Accounts
- Create account at [PyPI](https://pypi.org/account/register/)
- Create account at [Test PyPI](https://test.pypi.org/account/register/)
- Generate API tokens for authentication

### 3. Install Dependencies
```bash
# Install build tools
pip install build twine

# Install development dependencies
pip install -e ".[dev]"
```

## 🚀 Deployment Options

### Option 1: Using the Deployment Script (Recommended)
```bash
python deploy.py
```
The script will:
- Check requirements
- Run tests
- Build the package
- Upload to PyPI or Test PyPI

### Option 2: Manual Deployment

#### Test PyPI (for testing)
```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python -m build

# Check the package
python -m twine check dist/*

# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*

# Test installation
pip install -i https://test.pypi.org/simple/ ai-helper-agent
```

#### Production PyPI
```bash
# Upload to PyPI
python -m twine upload dist/*

# Test installation
pip install ai-helper-agent
```

## 🔑 Authentication

### Using API Tokens (Recommended)
1. Generate API tokens from PyPI/Test PyPI
2. Create `~/.pypirc`:
```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-your-api-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-your-test-api-token-here
```

## 📦 Post-Deployment

### Verify Installation
```bash
# Install your package
pip install ai-helper-agent

# Test the CLI
ai-helper --version

# Test the Python API
python -c "from ai_helper_agent import InteractiveAgent; print('Success!')"
```

### Update Documentation
- Add installation badges to README
- Update version numbers
- Tag the release in Git

## 🔄 Version Updates

For future releases:
1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Run tests
4. Build and deploy
5. Tag the release in Git

## 🚨 Important Notes

- **Test First**: Always deploy to Test PyPI first
- **Version Numbers**: Can't reuse version numbers on PyPI
- **Dependencies**: Make sure all dependencies are available on PyPI
- **License**: Ensure you have rights to publish the code
- **Backups**: Keep local backups of your releases

## 🎉 Success!

Once deployed, your package will be available at:
- **PyPI**: https://pypi.org/project/ai-helper-agent/
- **Installation**: `pip install ai-helper-agent`

Good luck with your deployment! 🚀
