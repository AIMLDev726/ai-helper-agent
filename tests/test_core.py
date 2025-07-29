"""
Test cases for AI Helper Agent core functionality
"""

import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ai_helper_agent.core import InteractiveAgent
from ai_helper_agent.utils import validate_python_code, run_python_code


class TestInteractiveAgent:
    """Test cases for InteractiveAgent class"""
    
    def test_agent_initialization(self):
        """Test agent can be initialized"""
        agent = InteractiveAgent(workspace_path=".")
        assert agent is not None
        assert agent.workspace_path.name in [".", "ai_helper_agent_final"]
    
    def test_system_prompt_setup(self):
        """Test system prompt is properly set"""
        agent = InteractiveAgent()
        assert agent.system_prompt is not None
        assert "CODE ANALYSIS" in agent.system_prompt
        assert "BUG FIXING" in agent.system_prompt


class TestUtils:
    """Test cases for utility functions"""
    
    def test_validate_python_code_valid(self):
        """Test validation of valid Python code"""
        result = validate_python_code("print('Hello World')")
        assert result["valid"] is True
        assert result["error"] is None
    
    def test_validate_python_code_invalid(self):
        """Test validation of invalid Python code"""
        result = validate_python_code("print('Hello World'")  # Missing closing parenthesis
        assert result["valid"] is False
        assert result["error"] is not None
        assert "Syntax error" in result["error"]
    
    def test_run_python_code_success(self):
        """Test running valid Python code"""
        result = run_python_code("print('test')")
        assert result["success"] is True
        assert "test" in result["stdout"]
        assert result["returncode"] == 0
    
    def test_run_python_code_error(self):
        """Test running invalid Python code"""
        result = run_python_code("raise ValueError('test error')")
        assert result["success"] is False
        assert "test error" in result["stderr"]
        assert result["returncode"] != 0


if __name__ == "__main__":
    pytest.main([__file__])
