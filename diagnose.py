# diagnose.py - Check setup and dependencies
import os
import sys
from pathlib import Path

def check_setup():
    print("🔍 Diagnosing Transit Safety API Setup...")
    print(f"Python version: {sys.version}")
    print(f"Current directory: {os.getcwd()}")
    
    # Check required files
    required_files = [
        'main.py', 'database.py', 'subway_stations.py', 
        'ml_integration.py', 'run.py', 'requirements.txt', '.env'
    ]
    
    print("\n📁 Checking required files:")
    missing_files = []
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            missing_files.append(file)
    
    # Check dependencies
    print("\n📦 Checking dependencies:")
    required_packages = [
        'fastapi', 'uvicorn', 'pydantic', 'python-dotenv', 
        'exa_py', 'cerebras_cloud_sdk', 'geopy', 'sqlalchemy'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_').replace('_py', ''))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - NOT INSTALLED")
            missing_packages.append(package)
    
    # Check environment variables
    print("\n🔐 Checking environment variables:")
    required_vars = ['EXA_API_KEY', 'CEREBRAS_API_KEY']
    
    # Try to load .env file
    try:
        from dotenv import load_dotenv
        load_dotenv()
        print("✅ .env file loaded")
    except Exception as e:
        print(f"⚠️  .env file issue: {e}")
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if value and value != f"{var}":  # Check it's not the placeholder
            print(f"✅ {var} (set)")
        else:
            print(f"❌ {var} - NOT SET OR PLACEHOLDER")
            missing_vars.append(var)
    
    # Test basic imports
    print("\n🧪 Testing core imports:")
    try:
        from main import app
        print("✅ main.app imported successfully")
    except Exception as e:
        print(f"❌ Failed to import main.app: {e}")
        return False
    
    try:
        from database import create_tables
        print("✅ database functions imported successfully")
    except Exception as e:
        print(f"❌ Failed to import database: {e}")
    
    # Summary
    print(f"\n📋 Summary:")
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
    if missing_vars:
        print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
    
    if not missing_files and not missing_packages and not missing_vars:
        print("✅ All checks passed! Setup looks good.")
        return True
    else:
        print("⚠️  Issues found. Please fix the above problems.")
        return False

if __name__ == "__main__":
    setup_ok = check_setup()
    
    if setup_ok:
        print("\n🚀 Attempting to start server...")
        try:
            import uvicorn
            from main import app
            print("Starting server on http://localhost:8000")
            print("Press Ctrl+C to stop")
            uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
        except Exception as e:
            print(f"❌ Failed to start server: {e}")
    else:
        print("\n🛠️  Fix the issues above before starting the server.")