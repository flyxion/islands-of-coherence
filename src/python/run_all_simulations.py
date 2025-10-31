#!/usr/bin/env python3
import os
import subprocess

print("Running Islands of Coherence simulations...")

scripts = [
    "coherence_attractors.py",
    "monopole_nucleation.py",
    "clio_hydra_demo.py"
]

for script in scripts:
    print(f"Running {script}...")
    result = subprocess.run(['python', f'simulations/{script}'], cwd='/app')
    if result.returncode != 0:
        print(f"{script} failed!")
        exit(1)

print("All simulations complete!")
