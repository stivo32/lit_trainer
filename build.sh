#!/bin/bash
source venv/bin/activate
pyinstaller cli.spec
mv dist/cli dist/lit_trainer
cp dist/lit_trainer .
rm -rf build
rm -rf dist
deactivate