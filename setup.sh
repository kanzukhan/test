#!/bin/bash
set -e

echo "Installing ReconRad dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
