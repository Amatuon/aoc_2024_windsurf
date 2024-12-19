#!/bin/bash

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Deactivate virtual environment
deactivate

echo "Virtual environment setup complete!"
