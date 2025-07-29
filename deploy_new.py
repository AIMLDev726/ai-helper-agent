#!/usr/bin/env python3
"""
Enhanced deployment script for AI Helper Agent package.
"""

import subprocess
import sys
import os
import shutil
from pathlib import Path


def run_command(cmd, description, check=True):
    """Run a command and handle errors."""
    print(f"\n🔧 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"STDERR: {e.stderr}")
        return False


def check_requirements():
    """Check if required tools are installed."""
    print("🔍 Checking requirements...")
    
    required_tools = ['build', 'twine']
    missing_tools = []
    
    for tool in required_tools:
        if not run_command(f"python -m {tool} --help", f"Checking {tool}", check=False):
            missing_tools.append(tool)
    
    if missing_tools:
        print(f"\n❌ Missing required tools: {', '.join(missing_tools)}")
        print("📦 Installing missing tools...")
        for tool in missing_tools:
            if not run_command(f"pip install {tool}", f"Installing {tool}"):
                return False
    
    return True


def clean_build():
    """Clean previous build artifacts."""
    print("\n🧹 Cleaning previous builds...")
    
    dirs_to_clean = ['build', 'dist', '*.egg-info']
    
    for pattern in dirs_to_clean:
        for path in Path('.').glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"  Removed: {path}")
            elif path.is_file():
                path.unlink()
                print(f"  Removed: {path}")


def run_tests():
    """Run package tests."""
    print("\n🧪 Running tests...")
    
    # Run our CLI tests
    if not run_command("python test_cli.py", "Running CLI tests"):
        return False
    
    # Run package tests if they exist
    if not run_command("python test_package.py", "Running package tests"):
        return False
    
    return True


def build_package():
    """Build the package."""
    print("\n🏗️ Building package...")
    
    if not run_command("python -m build", "Building wheel and source distribution"):
        return False
    
    # List built files
    dist_files = list(Path('dist').glob('*'))
    if dist_files:
        print("\n📦 Built files:")
        for file in dist_files:
            print(f"  - {file}")
    else:
        print("❌ No files were built!")
        return False
    
    return True


def check_package():
    """Check the built package."""
    print("\n✅ Checking package...")
    
    return run_command("python -m twine check dist/*", "Checking package with twine")


def upload_to_testpypi():
    """Upload to Test PyPI."""
    print("\n🚀 Uploading to Test PyPI...")
    print("📝 You'll need your Test PyPI credentials.")
    
    return run_command(
        "python -m twine upload --repository testpypi dist/*",
        "Uploading to Test PyPI"
    )


def upload_to_pypi():
    """Upload to PyPI."""
    print("\n🚀 Uploading to PyPI...")
    print("📝 You'll need your PyPI credentials.")
    print("⚠️  This will make your package publicly available!")
    
    confirm = input("\nAre you sure you want to upload to PyPI? (yes/no): ")
    if confirm.lower() != 'yes':
        print("❌ Upload cancelled.")
        return False
    
    return run_command(
        "python -m twine upload dist/*",
        "Uploading to PyPI"
    )


def main():
    """Main deployment function."""
    print("🚀 AI Helper Agent Deployment Script")
    print("=" * 50)
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print(f"📁 Working directory: {os.getcwd()}")
    
    # Step 1: Check requirements
    if not check_requirements():
        print("❌ Requirements check failed!")
        return False
    
    # Step 2: Clean previous builds
    clean_build()
    
    # Step 3: Run tests
    if not run_tests():
        print("❌ Tests failed!")
        return False
    
    # Step 4: Build package
    if not build_package():
        print("❌ Package build failed!")
        return False
    
    # Step 5: Check package
    if not check_package():
        print("❌ Package check failed!")
        return False
    
    print("\n✅ Package built successfully!")
    print("\n🎯 Next steps:")
    print("1. Test on Test PyPI: python deploy.py --test")
    print("2. Deploy to PyPI: python deploy.py --deploy")
    
    # Handle command line arguments
    if len(sys.argv) > 1:
        if '--test' in sys.argv:
            return upload_to_testpypi()
        elif '--deploy' in sys.argv:
            return upload_to_pypi()
    
    return True


if __name__ == "__main__":
    try:
        success = main()
        if success:
            print("\n🎉 Deployment script completed successfully!")
        else:
            print("\n❌ Deployment script failed!")
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️ Deployment cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
