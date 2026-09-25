#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
VENV_DIR = PROJECT_DIR / "steam_env"


def run(command):
    """Run a command and stop if it fails."""
    subprocess.run(command, check=True)


def main():
    # Check if the virtual environment already exists
    if VENV_DIR.exists():
        print("virtual_env already exist.")
        return

    print("Creating steam_env...")

    run([sys.executable, "-m", "venv", str(VENV_DIR)])

    print("venv created ✓")

    # Locate the Python executable in the virtual environment
    if os.name == "nt":
        venv_python = VENV_DIR / "Scripts" / "python.exe"
    else:
        venv_python = VENV_DIR / "bin" / "python"

    if not venv_python.exists():
        raise FileNotFoundError(
            f"Virtual environment Python was not found at: {venv_python}"
        )
    
    # Upgrade pip
    run([
        str(venv_python),
        "-m",
        "pip",
        "install",
        "--upgrade",
        "pip",
        "--quiet",
    ])

    # Install ipykernel
    run([
        str(venv_python),
        "-m",
        "pip",
        "install",
        "ipykernel",
        "--quiet",
    ])

    print("ipykernel installed ✓")

    # Register the environment as a Jupyter kernel
    run([
        str(venv_python),
        "-m",
        "ipykernel",
        "install",
        "--user",
        "--name=steam_env",
        '--display-name=Steam Thesis (M2)',
    ])

    print("Kernel registered ✓")
    print()
    print("Steam Thesis environment setup complete ✓")


if __name__ == "__main__":
    main()
