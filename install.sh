#!/bin/bash

if ! command -v ollama &>/dev/null; then
    echo "installing Ollama"
    curl -fsSL https://ollama.com/install.sh | sudo sh
fi

python3 -m venv venv
source venv/bin/activate
pip install pyperclip


chmod +x help_tool.py
sudo ln -sf "$(pwd)/help_tool.py" /usr/local/bin/help
echo "Installed. Follow this format: help 'your question'"