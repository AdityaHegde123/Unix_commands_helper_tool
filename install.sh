#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "--- Setting up dependencies ---"

if ! command -v ollama &>/dev/null; then
    echo "Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sudo sh
fi

if [ ! -d "$SCRIPT_DIR/venv" ]; then
    python3 -m venv "$SCRIPT_DIR/venv"
fi

"$SCRIPT_DIR/venv/bin/pip" install pyperclip

echo "--- Creating system command 'ask' ---"

sudo tee /usr/local/bin/ask > /dev/null <<EOF
#!/bin/bash
"$SCRIPT_DIR/venv/bin/python" "$SCRIPT_DIR/help_tool.py" "\$@"
EOF

sudo chmod +x /usr/local/bin/ask

echo "format: ask 'question'"