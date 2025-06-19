#!/bin/bash

# Top-level subjects in foundations
subjects=(
  linear_algebra
  probability
  statistics
  calculus
  model_evaluation
)

mkdir -p foundation

for subject in "${subjects[@]}"; do
  mkdir -p foundation/$subject/projects
  touch foundation/$subject/README.md
  touch foundation/$subject/notes.ipynb
  touch foundation/$subject/projects/.gitkeep

  echo "# ${subject//_/\ }" > foundation/$subject/README.md
done

echo "✅ Foundation folders created."

