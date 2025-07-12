#!/usr/bin/env bash

set -euo pipefail

echo "🔧 Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo "✅ Python setup complete."

echo "📚 Checking for pandoc..."
if ! command -v pandoc &> /dev/null; then
  echo "❌ pandoc not found. Please install it with: brew install pandoc"
fi

echo "📚 Checking for xelatex engine (via BasicTeX)..."
if ! command -v xelatex &> /dev/null; then
  echo "🔍 xelatex not found. Installing BasicTeX via Homebrew..."
  brew install --cask basictex
  sudo tlmgr update --self
  sudo tlmgr install collection-latexrecommended
fi

echo "🟢 Environment ready. To activate later: source .venv/bin/activate"
