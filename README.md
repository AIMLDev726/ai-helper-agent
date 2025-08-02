# 🤖 AI Helper Agent v2.0.1

![PyPI](https://img.shields.io/pypi/v/ai-helper-agent)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**The Most Advanced AI-Powered Programming Assistant** with multiple LLM providers, internet search, file processing, browser automation, MCP integration, and 40+ user-friendly CLI commands.

---

## 🌟 **Quick Start - User-Friendly Commands**

### **🚀 Main AI Chat Interfaces:**

```bash
# 🌟 FLAGSHIP - Most Powerful (FREE G4F + Internet Search)
ai-super-chat       # ⭐ RECOMMENDED - Free GPT-4 with web search
ai-smart            # Alternative name  
ai-genius           # Alternative name
ai-flagship         # Alternative name

# ⚡ FASTEST - Lightning Speed (Groq Only)
ai-fast-chat        # Ultra-fast responses with Groq
ai-quick            # Alternative name
ai-turbo            # Alternative name
ai-speed            # Alternative name

# 🌐 WEB SEARCH - Internet-Enabled (Groq + Web)
ai-web-chat         # Smart web search with Groq
ai-search           # Alternative name  
ai-internet         # Alternative name
ai-web              # Alternative name

# 🤖 MULTI-AI - All Providers (Groq, OpenAI, Anthropic, Google)
ai-smart-chat       # Choose any AI provider
ai-multi            # Alternative name
ai-pro              # Alternative name
ai-providers        # Alternative name

# 🔧 DEVELOPER - Advanced Features (File Processing + Multi-Provider)
ai-advanced         # Full developer toolkit
ai-dev              # Alternative name
ai-expert           # Alternative name
ai-coder            # Alternative name

# 📋 CLI SELECTOR - Interactive Menu
ai-menu             # Choose from visual menu
ai-chat-selector    # Alternative selector
ai-helper-selector  # Legacy selector
```

### **🛠️ System Tools & Utilities:**

```bash
# 🔑 API KEY MANAGEMENT
ai-setup-keys       # Interactive API key setup wizard
ai-keys             # Manage all API keys
ai-security         # Security and key management

# 🌐 BROWSER & WEB TOOLS
ai-browser          # Browser automation and web integration
ai-web-tools        # Alternative name

# 🔗 MCP INTEGRATION
ai-mcp              # Model Context Protocol integration
ai-context          # Alternative name

# ⚙️ CORE SYSTEM TOOLS
ai-core             # Core system functionality
ai-system           # Alternative name
ai-tools            # General tools

# 📊 LEGACY COMMANDS (Still Available)
ai-helper           # Original multi-provider CLI
ai-helper-multi     # Multi-provider (legacy)
ai-helper-single    # Single provider (legacy)
ai-helper-groq      # Groq-specific (legacy)
ai-helper-internet-single  # Internet single (legacy)
```

---

## 🔑 **API Key Setup & Security**

### **🚀 Quick Setup Commands:**

```bash
# 🎯 RECOMMENDED - Interactive Setup Wizard
ai-setup-keys       # Complete setup with guided wizard
ai-keys             # Alternative command
ai-security         # Alternative command

# 📝 Manual Setup Commands
python -m ai_helper_agent.utilities.api_key_setup

# Add keys for specific providers
python -m ai_helper_agent.utilities.api_key_setup add groq
python -m ai_helper_agent.utilities.api_key_setup add openai
python -m ai_helper_agent.utilities.api_key_setup add anthropic
python -m ai_helper_agent.utilities.api_key_setup add google

# View existing keys (masked for security)
python -m ai_helper_agent.utilities.api_key_setup list

# Test API key connections
python -m ai_helper_agent.utilities.api_key_setup test

# Remove keys
python -m ai_helper_agent.utilities.api_key_setup remove groq

# Show help
python -m ai_helper_agent.utilities.api_key_setup --help
```

### **🆓 No API Key Required Options:**

- **G4F (GPT4Free)**: Use `ai-super-chat` for FREE GPT-4 access
- **Local Models**: Coming soon with Ollama integration

### **🔐 Security Features:**
- ✅ **Encrypted Storage**: All keys encrypted at rest
- ✅ **Local Storage**: Keys never leave your machine
- ✅ **Masked Display**: Keys shown as `gsk_***...***xyz`
- ✅ **Secure Prompts**: Password-style input for keys

---

## 📦 **Installation**

### **Simple Installation:**
```bash
pip install ai-helper-agent
```

### **Development Installation:**
```bash
git clone https://github.com/AIMLDev726/ai-helper-agent
cd ai-helper-agent
pip install -e .
```

---

## 🎯 **Features Overview**

### **🌟 Core Capabilities**
- ✅ **Multi-Provider AI**: Groq, OpenAI, Anthropic, Google AI, G4F
- ✅ **Free G4F Access**: No API keys needed for GPT-4
- ✅ **Internet Search**: Real-time web access and current information
- ✅ **File Processing**: Analyze, modify, and generate files
- ✅ **Browser Automation**: Web integration and automation tools
- ✅ **MCP Integration**: Model Context Protocol support
- ✅ **Code Generation**: Natural language to code conversion
- ✅ **Rich UI**: Beautiful terminal interfaces with tables and formatting
- ✅ **Session Memory**: Persistent conversation history
- ✅ **40+ Commands**: User-friendly CLI ecosystem

### **🔧 Advanced Features**
- 🎨 **Syntax Highlighting**: Beautiful code rendering with Rich UI
- 🔍 **Smart Search**: AI decides when to search the web
- 💾 **Session Management**: Named sessions for different projects
- ⚡ **Streaming Responses**: Real-time response generation
- 🛡️ **Security Controls**: Encrypted API key storage
- 📁 **Workspace Integration**: Context-aware file operations
- 🌐 **Browser Tools**: Web automation and scraping capabilities
- 🔗 **MCP Protocol**: Advanced context management
- 📊 **Rich Help System**: Beautiful help for all commands

### **🎨 User Experience**
- 🎯 **Easy Commands**: Non-technical names like `ai-super-chat`
- 📋 **Interactive Menu**: Visual CLI selector with `ai-menu`
- 🎨 **Rich UI**: Tables, colors, and beautiful formatting
- ⚡ **Quick Access**: Aliases like `ai-quick`, `ai-search`
- 🔧 **Developer Tools**: Advanced features with `ai-advanced`

---

## 🚀 **Quick Examples**

### **🌟 Flagship - Free AI with Internet**
```bash
ai-super-chat        # Start the flagship experience

# Example conversations:
> "What's the latest Python 3.12 features with examples?"
> "How to deploy FastAPI to AWS in 2024?"
> "Show me the newest React 18 hooks with code examples"
> "Debug this error: ModuleNotFoundError tensorflow"
> "Latest Django 5.0 tutorial with step-by-step guide"
```

### **⚡ Lightning Fast Responses**
```bash
ai-quick             # Ultra-fast Groq responses

# Perfect for:
> "Write a Python function to sort a list"
> "Explain this code: async def main():"
> "Convert this to TypeScript: const data = []"
> "Fix this syntax error in my function"
```

### **🌐 Web-Enabled Development**
```bash
ai-search            # Internet-powered development

# Ideal for:
> "Latest Django 5.0 tutorial with examples"
> "Current best practices for React 18 in 2024"
> "How to fix CORS errors in Express.js latest version"
> "Compare FastAPI vs Flask performance 2024"
```

### **🤖 Multi-Provider Power**
```bash
ai-multi             # Choose your AI provider

# Available providers:
# - Groq (Ultra-fast, 1000+ tokens/sec)
# - OpenAI (GPT-4, most capable)
# - Anthropic (Claude, great for code analysis)
# - Google (Gemini, multimodal capabilities)
# - G4F (Free GPT-4 access)
```

### **🔧 Developer Toolkit**
```bash
ai-dev               # Advanced development features

# Advanced capabilities:
> "Analyze all Python files in this project"
> "Review this code for security vulnerabilities"
> "Generate comprehensive unit tests for my functions"
> "Optimize the performance of this entire codebase"
> "Create documentation for this API"
```

### **🛠️ System Tools**
```bash
# Browser automation and web tools
ai-browser           # Web automation features

# MCP integration for advanced context
ai-mcp               # Model Context Protocol tools

# Core system functionality
ai-core              # Core system tools and utilities
```

---

## 📚 **Complete Command Reference**

### **🎯 Main Chat CLIs:**
| Command | Purpose | Features |
|---------|---------|----------|
| `ai-super-chat` | 🌟 Flagship (FREE G4F + Internet) | Free GPT-4, Web search, Rich UI |
| `ai-fast-chat` | ⚡ Ultra-fast (Groq only) | Lightning speed, 1000+ tokens/sec |
| `ai-web-chat` | 🌐 Internet-enabled (Groq + Web) | Smart web search, current info |
| `ai-smart-chat` | 🤖 Multi-provider | All AI providers, model selection |
| `ai-advanced` | 🔧 Developer toolkit | File processing, code analysis |
| `ai-menu` | 📋 Interactive selector | Visual CLI chooser |

### **🛠️ System & Utility Commands:**
| Command | Purpose | Features |
|---------|---------|----------|
| `ai-setup-keys` | 🔑 API key management | Interactive wizard, secure setup |
| `ai-browser` | 🌐 Browser automation | Web scraping, automation tools |
| `ai-mcp` | 🔗 MCP integration | Model Context Protocol |
| `ai-core` | ⚙️ Core system tools | System functionality |

### **⚡ Quick Access Aliases:**
| Alias | Main Command | Usage |
|-------|-------------|--------|
| `ai-quick` | `ai-fast-chat` | Ultra-fast responses |
| `ai-search` | `ai-web-chat` | Internet-powered queries |
| `ai-multi` | `ai-smart-chat` | Multi-provider access |
| `ai-dev` | `ai-advanced` | Developer features |
| `ai-keys` | `ai-setup-keys` | Key management |

---

## 🐍 **Python API Usage**

### **Basic Usage:**
```python
from ai_helper_agent import create_agent

# Create an agent instance
agent = create_agent()

# Ask for help
response = agent.process_request("How do I implement a binary search in Python?")
print(response)
```

### **Advanced Configuration:**
```python
from ai_helper_agent import InteractiveAgent
from ai_helper_agent.config import config

# Customize configuration
config.update({
    'temperature': 0.7,
    'max_tokens': 2048,
    'provider': 'groq',
    'model': 'llama-3.1-70b'
})

# Create agent with custom settings
agent = InteractiveAgent()
```

### **File Operations:**
```python
from ai_helper_agent import InteractiveAgent

agent = InteractiveAgent()

# Analyze a file
response = agent.process_request("Analyze the code in myfile.py")

# Get optimization suggestions  
response = agent.process_request("Optimize the performance of myfile.py")

# Generate unit tests
response = agent.process_request("Create unit tests for functions in mymodule.py")
```

### **Internet-Enabled Queries:**
```python
from ai_helper_agent import InternetAgent

# Create internet-enabled agent
agent = InternetAgent()

# Ask current questions
response = agent.process_request("What are the latest Python 3.12 features?")

# Technical documentation queries
response = agent.process_request("Show me FastAPI async database examples")
```

### **🎨 Rich Help System**
Every CLI has beautiful, comprehensive help:

```bash
ai-super-chat --help     # Flagship features and commands
ai-web-chat --help       # Internet search capabilities  
ai-advanced --help       # Developer toolkit overview
ai-smart-chat --help     # Multi-provider options
```

### **🔄 Session Management**
```bash
# Named sessions for different projects
ai-dev --session backend-api
ai-search --session frontend-bugs
ai-quick --session quick-scripts

# Quick mode (skip startup)
ai-super-chat --quick
ai-multi --quick
```

### **🌐 Internet Features**

#### **Permission Levels:**
- **Smart** (Default): AI decides when to search
- **Always**: Search for every query  
- **Ask**: Prompt before searching
- **Never**: Disable internet access

#### **Internet Commands (in chat):**
```bash
# Manual search
> internet search "latest React features"

# Change permissions  
> internet permission smart
> internet permission always
> internet permission ask
> internet permission never

# Check status
> internet
```

### **🤖 Provider-Specific Features**

#### **Groq (Ultra-Fast)**
- Models: Llama 3.1, Llama 3.3, Mixtral, Gemma
- Speed: ~1000 tokens/second
- Best for: Quick responses, coding tasks

#### **OpenAI (Most Capable)**  
- Models: GPT-4, GPT-4 Turbo, GPT-3.5 Turbo
- Best for: Complex reasoning, creative tasks

#### **Anthropic (Code Expert)**
- Models: Claude 3.5 Sonnet, Claude 3 Haiku  
- Best for: Code analysis, safety-focused tasks

#### **Google (Multimodal)**
- Models: Gemini Pro, Gemini 1.5 Pro
- Best for: Mixed content, vision tasks

#### **G4F (Free GPT-4)**
- Models: GPT-4, GPT-3.5, Various others
- Cost: 100% Free
- Best for: General use without API costs

---

## 🛠️ **Configuration & Setup**

### **Environment Variables**
```bash
# Optional: Set default provider
export AI_HELPER_DEFAULT_PROVIDER=groq

# Optional: Set default model
export AI_HELPER_DEFAULT_MODEL=llama-3.1-70b

# Optional: Custom workspace
export AI_HELPER_WORKSPACE=/path/to/project
```

### **Config File (Optional)**
Create `~/.ai-helper-agent/config.yaml`:
```yaml
default_provider: groq
default_model: llama-3.1-70b
temperature: 0.7
max_tokens: 4096
internet_permission: smart
session_persistence: true
```

---

## 🔐 **Security & Privacy**

### **API Key Security**
- ✅ **Encrypted Storage**: All keys encrypted at rest
- ✅ **Local Storage**: Keys never leave your machine
- ✅ **Masked Display**: Keys shown as `gsk_***...***xyz`
- ✅ **Secure Prompts**: Password-style input for keys

### **Internet Privacy**
- ✅ **User Control**: You control when internet is accessed
- ✅ **Transparent**: AI tells you when it searches
- ✅ **Configurable**: Set permission levels
- ✅ **No Tracking**: Searches are not logged or tracked

### **File Security**
- ✅ **Workspace Isolation**: Operations limited to workspace
- ✅ **Permission Checks**: Confirms before file modifications
- ✅ **Backup Options**: Can create backups before changes
- ✅ **Read-Only Mode**: Available for analysis-only tasks

---

## 🎯 **Use Cases & Examples**

### **🚀 Web Development**
```bash
ai-search

> "Create a Next.js 14 app with TypeScript and Tailwind"
> "How to implement authentication with NextAuth.js?"  
> "Debug CORS issues in my Express API"
> "Latest React 18 best practices for state management"
```

### **🐍 Python Development**
```bash
ai-dev

> "Analyze this Flask app for security vulnerabilities"
> "Generate FastAPI endpoints from this database schema"
> "Optimize this pandas data processing code"
> "Create unit tests for all functions in this file"
```

### **📱 Mobile Development**
```bash
ai-multi --provider anthropic

> "Convert this React component to React Native"
> "Create Flutter widgets for this design"
> "Implement SwiftUI navigation patterns"
> "Debug Android build.gradle dependencies"
```

### **🔬 Data Science**
```bash
ai-super-chat

> "What's the latest in machine learning frameworks?"
> "Create a PyTorch model for image classification"  
> "Analyze this dataset and suggest visualizations"
> "Compare TensorFlow vs PyTorch for NLP tasks"
```

### **☁️ DevOps & Deployment**
```bash
ai-expert

> "Create Docker setup for this Python app"
> "Generate Kubernetes deployment manifests"
> "Set up CI/CD pipeline for GitHub Actions"
> "Configure AWS Lambda deployment with Terraform"
```

---

## 🚨 **Troubleshooting**

### **Common Issues**

#### **"Command not found" Error**
```bash
# Reinstall to fix PATH issues
pip install --force-reinstall ai-helper-agent

# Or use Python module syntax
python -m ai_helper_agent.cli.cli_selector
```

#### **API Key Issues**
```bash
# Check if keys are set
python -m ai_helper_agent.utilities.api_key_setup list

# Test connections
python -m ai_helper_agent.utilities.api_key_setup test

# Re-add problematic keys
python -m ai_helper_agent.utilities.api_key_setup add groq
```

#### **Internet Search Not Working**
```bash
# Check internet permission
> internet

# Enable internet access
> internet permission smart

# Manual search test
> internet search "test query"
```

#### **Rich UI Display Issues**
```bash
# Update Rich library
pip install --upgrade rich

# Check terminal compatibility
python -c "from rich.console import Console; Console().print('✅ Rich working')"
```

---

## 🔄 **Version History**

### **v2.0.1 (Current) - August 2025**
- ✅ **User-Friendly Commands**: Easy-to-remember CLI names
- ✅ **Rich UI Help**: Beautiful help system for all CLIs
- ✅ **Fixed Coroutine Issues**: Resolved async/await problems
- ✅ **Enhanced Security**: Improved API key management
- ✅ **Command Aliases**: Multiple names for each CLI
- ✅ **Better Error Handling**: More helpful error messages

### **v1.0.0 - JUly 2024**
- 🌟 **G4F Integration**: Free GPT-4 access
- 🌐 **Internet Search**: Real-time web access
- 🎨 **Rich UI**: Beautiful terminal interfaces
- 🔧 **File Processing**: Advanced file operations
- 📁 **Session Management**: Named conversation sessions
---

## 📖 **Documentation Links**

- **🏠 Homepage**: [GitHub Repository](https://github.com/AIMLDev726/ai-helper-agent)
- **🐛 Issues**: [Bug Tracker](https://github.com/AIMLDev726/ai-helper-agent/issues)  
- **📝 Changelog**: [Full Version History](CHANGELOG.md)
- **🤝 Contributing**: [Contribution Guide](CONTRIBUTING.md)
- **📜 License**: [MIT License](LICENSE)

---

## 🌍 **Community & Support**

### **Getting Help**
- 📧 **Email**: aistudentlearn4@gmail.com
- 🐛 **GitHub Issues**: Report bugs and request features
- 💬 **Discussions**: Share tips and ask questions

### **Contributing**
We welcome contributions! Areas where you can help:
- 🐛 Bug fixes and improvements
- 📚 Documentation updates  
- 🌟 New features and integrations
- 🧪 Testing and quality assurance

---

## 📄 **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**Free for personal and commercial use!** ✅

---

## 🙏 **Acknowledgments**

- **🚀 Built with**: [LangChain](https://langchain.com/) framework
- **🎨 UI powered by**: [Rich](https://rich.readthedocs.io/) library  
- **🤖 AI providers**: Groq, OpenAI, Anthropic, Google, G4F
- **💡 Inspired by**: GitHub Copilot, ChatGPT, and the open-source community

---

## 🎉 **Ready to Get Started?**

```bash
# Install
pip install ai-helper-agent

# Try the flagship (free!)
ai-super-chat

# Or choose your interface
ai-menu
```

**Happy Coding with AI! 🚀✨**

---

**Made with ❤️ by [AIMLDev726](https://github.com/AIMLDev726)**
