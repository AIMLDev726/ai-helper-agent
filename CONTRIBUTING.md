# AI Helper Agent

## How to Contribute

Thank you for your interest in contributing to AI Helper Agent! This document provides guidelines for contributing to the project.

### Development Setup

1. **Fork and Clone the Repository**
   ```bash
   git clone https://github.com/AIMLDev726/ai-helper-agent.git
   cd ai-helper-agent
   ```

2. **Set Up Development Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   
   # Install development dependencies
   pip install -r requirements-dev.txt
   
   # Install in development mode
   pip install -e .
   ```

3. **Install Pre-commit Hooks**
   ```bash
   pre-commit install
   ```

### Code Style

- We use **Black** for code formatting
- We use **flake8** for linting
- We use **mypy** for type checking
- Follow PEP 8 guidelines

### Testing

- Write tests for all new features
- Ensure all tests pass before submitting PR
- Maintain test coverage above 80%

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=ai_helper_agent
```

### Submitting Changes

1. Create a feature branch
2. Make your changes
3. Add tests
4. Run the test suite
5. Submit a pull request

### Code Review Process

- All submissions require review
- We may suggest changes
- Once approved, we'll merge your PR

### Reporting Issues

- Use GitHub issues
- Provide clear description
- Include reproduction steps
- Add relevant labels

### Questions?

Feel free to open an issue for any questions about contributing!
