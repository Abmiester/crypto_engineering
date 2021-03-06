#!/bin/bash

echo "Requirements: npm (JS package manager) and poetry (Python package manager)"

# Install Python dependencies
poetry install

# Recompile frontend code
npm install
npm run webpack

# Run 4 nodes and kill all of them if one process is killed
killbg() {
        for p in "${pids[@]}" ; do
                kill "$p";
        done
}

python3 -m webbrowser "http://localhost:5000"

trap killbg EXIT
pids=()
python3 node.py 5000 &
pids+=($!)
python3 node.py 5001 5000 &
pids+=($!)
python3 node.py 5002 5001 &
pids+=($!)
python3 node.py 5003 5002
pids+=($!)
