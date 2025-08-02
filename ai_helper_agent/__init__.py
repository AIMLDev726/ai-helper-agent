"""
AI Helper Agent - Interactive AI Assistant for Programming

A comprehensive AI-powered programming assistant with advanced code generation,
analysis, debugging, and optimization capabilities using multiple LLM providers.

Features:
- Code generation from natural language descriptions
- Intelligent code completion and suggestions
- Cross-language code translation
- Advanced debugging and optimization
- File operations with security controls
- Search functionality across codebases
- Interactive CLI with conversation history
- Support for multiple programming languages
- Multi-provider support (Groq, OpenAI, Anthropic, Google, Ollama)
- Internet-enabled AI with web search capabilities

Latest enhancements:
- Organized project structure for better maintainability
- Updated to latest Groq models (Llama 3.1, Llama 3.3, Gemma 2, etc.)
- Enhanced file creation with proper permissions handling
- Advanced search functionality for files and content
- Codex-like capabilities for professional development
- Improved security manager with better file access controls
"""

# Core functionality
try:
    from .core.core import InteractiveAgent, create_agent
    from .core.config import config
    from .core.security import security_manager
except ImportError:
    # Fallback for backwards compatibility
    try:
        from .core import InteractiveAgent, create_agent
        from .config import config
        from .security import security_manager
    except ImportError:
        # Final fallback
        InteractiveAgent = None
        create_agent = None
        config = None
        security_manager = None

# Utilities
try:
    from .utils.utils import validate_python_code, run_python_code, format_code_output
except ImportError:
    try:
        from .utils import validate_python_code, run_python_code, format_code_output
    except ImportError:
        validate_python_code = None
        run_python_code = None
        format_code_output = None

# CLI functionality - backwards compatibility
try:
    from .cli.cli_multi_provider import MultiProviderAIHelperCLI as AIHelperCLI
    from .cli.cli_multi_provider import main
except ImportError:
    try:
        from .cli import AIHelperCLI, main
    except ImportError:
        AIHelperCLI = None
        main = None

__version__ = "2.0.1"
__author__ = "AIMLDev726"
__email__ = "aistudentlearn4@gmail.com"

__all__ = [
    "InteractiveAgent",
    "create_agent",
    "validate_python_code", 
    "run_python_code",
    "format_code_output",
    "config",
    "AIHelperCLI",
    "main",
    "security_manager"
]

# Package metadata
__title__ = "ai-helper-agent"
__description__ = "Interactive AI Helper Agent for code assistance, analysis, and bug fixing with multi-provider support"
__url__ = "https://github.com/AIMLDev726/ai-helper-agent"
__license__ = "MIT"