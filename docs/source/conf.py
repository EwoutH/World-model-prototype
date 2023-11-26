# Minimal conf.py for Sphinx documentation

# -- Project information -----------------------------------------------------

project = "World model prototype"
author = "Ewout ter Hoeven"

# -- General configuration ---------------------------------------------------

extensions = []

# -- Add policy, behaviors and docs/source to path --------------------------------------
import os
import sys
import glob

sys.path.insert(0, os.path.abspath("../.."))

source_dirs = ["policy", "docs/source"]

# Use glob to find all README.md files in src/behaviors and its subdirectories
behaviors_readmes = glob.glob(
    os.path.join(os.path.dirname(__file__), "../../src/behaviors/**/README.md"),
    recursive=True,
)
policy_docs = glob.glob(
    os.path.join(os.path.dirname(__file__), "../../policy/**/*.md"), recursive=True
)

# Define the toctree with the dynamically generated list of README.md files
toctree_behaviors = [
    "src/behaviors/" + os.path.relpath(readme, os.path.dirname(__file__))
    for readme in behaviors_readmes
]
toctree_policy = [
    "policy/" + os.path.relpath(doc, os.path.dirname(__file__)) for doc in policy_docs
]

# Append the dynamically generated list of README.md files to the TOCTREE
source_dirs.extend(toctree_behaviors)
