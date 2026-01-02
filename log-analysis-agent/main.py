"""
Log Analysis Agent - Main Entry Point
Simple test script to verify setup
"""

import sys
import os
from pathlib import Path

def check_setup():
    """Verify project structure and dependencies"""
    print("=" * 60)
    print("Log Analysis Agent - Setup Verification")
    print("=" * 60)
    
    # Check Python version
    print(f"\n✓ Python version: {sys.version.split()[0]}")
    
    # Check project structure
    project_root = Path(__file__).parent
    print(f"✓ Project root: {project_root}")
    
    required_dirs = [
        "config",
        "data/sample_logs",
        "data/models",
        "data/database",
        "src/core",
        "src/models",
        "src/analysis",
    ]
    
    print("\nChecking directory structure:")
    all_exist = True
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        exists = full_path.exists()
        symbol = "✓" if exists else "✗"
        print(f"  {symbol} {dir_path}")
        if not exists:
            all_exist = False
    
    # Check required files
    required_files = [
        "README.md",
        "requirements.txt",
        "config/config.yaml",
        "config/log_patterns.json",
    ]
    
    print("\nChecking required files:")
    for file_path in required_files:
        full_path = project_root / file_path
        exists = full_path.exists()
        symbol = "✓" if exists else "✗"
        print(f"  {symbol} {file_path}")
        if not exists:
            all_exist = False
    
    # Try importing key packages
    print("\nChecking dependencies:")
    packages = [
        ("numpy", "NumPy"),
        ("pandas", "Pandas"),
        ("sklearn", "scikit-learn"),
        ("yaml", "PyYAML"),
    ]
    
    for package, name in packages:
        try:
            __import__(package)
            print(f"  ✓ {name}")
        except ImportError:
            print(f"  ✗ {name} - NOT INSTALLED")
            all_exist = False
    
    # Summary
    print("\n" + "=" * 60)
    if all_exist:
        print("✓ Setup verification PASSED!")
        print("\nNext steps:")
        print("1. Add your log files to: data/sample_logs/")
        print("2. Ready to build the Log Parser module!")
    else:
        print("✗ Setup verification FAILED!")
        print("\nPlease:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Verify all directories and files exist")
    print("=" * 60)

if __name__ == "__main__":
    check_setup()
