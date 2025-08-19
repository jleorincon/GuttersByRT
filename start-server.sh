#!/bin/bash

# Gutters by RT - Local Server Startup Script
# This script starts a local web server to host the website

echo "🏠 Starting Gutters by RT Local Server..."
echo "========================================="

# Check if Python is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Error: Python is not installed or not in PATH"
    echo "Please install Python 3 and try again"
    exit 1
fi

echo "✅ Using Python: $PYTHON_CMD"

# Change to script directory
cd "$(dirname "$0")"

# Start the server
echo "🚀 Starting server..."
$PYTHON_CMD server.py
