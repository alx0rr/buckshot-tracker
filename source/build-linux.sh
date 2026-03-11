#!/bin/bash
set -e

echo ""
echo "  Building Buckshot Tracker for Linux..."
echo ""

pyinstaller \
  --onefile \
  --name server \
  --add-data "buckshot-tracker.html:." \
  --icon icon.ico \
  server.py

mkdir -p ../linux-app
cp dist/server ../linux-app/server
chmod +x ../linux-app/server

rm -rf build dist __pycache__ server.spec

echo ""
echo "  Done! Binary: ../linux-app/server"
echo ""