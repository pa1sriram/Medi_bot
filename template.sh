#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status
set -x  # Print each command before executing it

#Creating directory
mkdir -p src
mkdir -p research

#Creating files
#Constructor file init
touch src/__init__.py
touch src/helper.py
touch src/prompt.py
#To store environment secrets like storing pine code secrets or open AI keys we created env
touch .env
touch setup.py
touch app.py
touch research/trails.ipynb
touch requirements.txt

echo "Project structure created successfully."