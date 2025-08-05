# Quick Start Guide 🚀

Get your help tool running in 3 simple steps!

## Step 1: Install Ollama
```bash
# Download and install from https://ollama.ai/
# Or on macOS with Homebrew:
brew install ollama
```

## Step 2: Pull a Model
```bash
# Start Ollama
ollama serve

# In another terminal, pull a model
ollama pull llama3.2
```

## Step 3: Install the Help Tool
```bash
# Make the installer executable and run it
chmod +x install.sh
./install.sh
```

## Test It! 🎉
```bash
help "how to find all PDF files"
help "how to check disk space"
help "how to kill a process"
```

## That's it! 

You now have a powerful terminal assistant that can help you with any Unix/Linux command. Just ask what you want to do in plain English!

### Need help?
- Run `python3 test_installation.py` to check your setup
- See the full README.md for detailed documentation
- Make sure Ollama is running: `ollama serve` 