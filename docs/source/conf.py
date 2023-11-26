# -- Project information -----------------------------------------------------
project = "World model prototype"
author = "Ewout ter Hoeven"

# -- General configuration ---------------------------------------------------
extensions = ["recommonmark"]  # Add recommonmark for Markdown support

# -- Path setup --------------------------------------------------------------
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

behaviors_dir = '../../src/behaviors'
toctree_entries = []

for behavior in os.listdir(behaviors_dir):
    behavior_path = os.path.join(behaviors_dir, behavior)
    if os.path.isdir(behavior_path):
        readme_path = os.path.join(behavior_path, 'README.md')
        if os.path.exists(readme_path):
            # Assuming the README files are named 'README.md'
            toctree_entries.append(f"{behavior_path}/README")

# Write to a file that can be included in your Sphinx documentation
with open('behavior_toctree.rst', 'w') as file:
    file.write(".. toctree::\n")
    for entry in toctree_entries:
        file.write(f"   {entry}\n")
