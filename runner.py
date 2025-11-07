#!/usr/bin/env python3
"""
Simple test runner to debug the configuration
"""
import subprocess
import sys
import os

def run_tests():
    """Run pytest with our custom arguments."""
    # Ensure reports directory exists
    os.makedirs("reports", exist_ok=True)
    
    cmd = [
        sys.executable,  # Use the same Python interpreter
        "-m", "pytest",
        "-v",
        "--tb=short",    # shorter tracebacks
        #"--strict-markers",
        #"--html=reports/report.html",
        #"--self-contained-html",
        # Remove these if they're not defined in your pytest configuration
        # "--env=uat",
        # "--customer=common",
        #"features/",
        #"-m", "uat"
    ]
    
    print("🚀 Selenium UI Test Runner")
    print("=" * 50)
    print("Running command:", " ".join(cmd))
    print("=" * 50)
    
    result = subprocess.run(cmd)
    
    # Print meaningful messages based on exit code
    if result.returncode == 0:
        print("✅ All tests passed!")
    elif result.returncode == 1:
        print("❌ Some tests failed")
    elif result.returncode == 2:
        print("❌ Test execution was interrupted")
    elif result.returncode == 3:
        print("❌ Internal error occurred")
    elif result.returncode == 4:
        print("❌ No tests were collected")
    elif result.returncode == 5:
        print("❌ No tests were found")
    
    return result.returncode

if __name__ == "__main__":
    sys.exit(run_tests())