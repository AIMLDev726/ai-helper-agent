"""
Test cases for AI Helper Agent utility functions
"""

import pytest
import sys
import os
import tempfile
import pathlib

# Add the parent directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ai_helper_agent.utils import (
    validate_python_code, 
    run_python_code,
    format_code_output
)


class TestCodeValidation:
    """Test code validation utilities"""
    
    def test_valid_simple_code(self):
        """Test validation of simple valid code"""
        code = "x = 1 + 2"
        result = validate_python_code(code)
        assert result["valid"] is True
        assert result["error"] is None
    
    def test_valid_function_code(self):
        """Test validation of function definition"""
        code = """
def hello_world():
    return "Hello, World!"
        """
        result = validate_python_code(code)
        assert result["valid"] is True
    
    def test_invalid_syntax(self):
        """Test detection of syntax errors"""
        code = "if True"  # Missing colon
        result = validate_python_code(code)
        assert result["valid"] is False
        assert "Syntax error" in result["error"]
    
    def test_invalid_indentation(self):
        """Test detection of indentation errors"""
        code = """
def test():
print("hello")
        """
        result = validate_python_code(code)
        assert result["valid"] is False


class TestCodeExecution:
    """Test code execution utilities"""
    
    def test_simple_execution(self):
        """Test execution of simple code"""
        code = "print('Hello, Test!')"
        result = run_python_code(code)
        assert result["success"] is True
        assert "Hello, Test!" in result["stdout"]
    
    def test_math_execution(self):
        """Test execution of mathematical operations"""
        code = "print(2 + 2)"
        result = run_python_code(code)
        assert result["success"] is True
        assert "4" in result["stdout"]
    
    def test_error_handling(self):
        """Test error handling in code execution"""
        code = "x = 1 / 0"  # Division by zero
        result = run_python_code(code)
        assert result["success"] is False
        assert "ZeroDivisionError" in result["stderr"]
    
    def test_timeout_handling(self):
        """Test timeout handling"""
        code = """
import time
time.sleep(0.1)
print("done")
        """
        result = run_python_code(code, timeout=1)
        assert result["success"] is True
        assert "done" in result["stdout"]


class TestCodeFormatting:
    """Test code formatting utilities"""
    
    def test_format_success_output(self):
        """Test formatting of successful output"""
        result = {
            "success": True,
            "stdout": "Hello World\n",
            "stderr": "",
            "returncode": 0
        }
        formatted = format_code_output(result)
        assert "✅ Success" in formatted
        assert "Hello World" in formatted
    
    def test_format_error_output(self):
        """Test formatting of error output"""
        result = {
            "success": False,
            "stdout": "",
            "stderr": "NameError: name 'x' is not defined\n",
            "returncode": 1
        }
        formatted = format_code_output(result)
        assert "❌ Error" in formatted
        assert "NameError" in formatted


if __name__ == "__main__":
    pytest.main([__file__])
