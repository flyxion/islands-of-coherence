#!/usr/bin/env python3
import sys
import os

# Add /app to Python path
sys.path.insert(0, '/app')

print("Running Islands of Coherence simulations...")

scripts = [
    "coherence_attractors.py",
    "monopole_nucleation.py",
    "clio_hydra_demo.py"
]

for script in scripts:
    print(f"Running simulations/{script}...")
    result = os.system(f'python simulations/{script}')
    if result != 0:
        print(f"{script} failed!")
        sys.exit(1)

print("All simulations complete!")
