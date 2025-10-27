import os
import sys
import subprocess

def install_requirements():
    """Installs required dependencies listed in requirements.txt"""
    print("Installing dependencies...\n")

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("\n✅ All dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print("\n❌ Installation failed!")
        print("Error details:", e)
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
