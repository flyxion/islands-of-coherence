#!/usr/bin/env python3
import os
import subprocess

notebooks = [
    "gauge_theory.ipynb",
    "monopole_nucleation.ipynb"
]

for nb in notebooks:
    print(f"Running {nb}...")
    subprocess.run([
        "jupyter", "nbconvert", "--to", "pdf",
        "--execute", "--no-input",
        f"notebooks/{nb}"
    ], check=True)

print("All simulations complete. Outputs in /output/")
