# Help Tool 🚀

A terminal assistant for new developers who want to learn Unix/Linux commands. Simply ask what you want to do, and get the exact command you need!

## What it does

Instead of memorizing Unix commands, just ask the `help` tool what you want to accomplish:

```bash
help "how to find all PDF files"
help "how to check disk space"
help "how to kill a process"
help "how to search for text in files"
```

The tool uses Ollama (local AI) to understand your request and provide the exact command you need, along with explanations.

## Prerequisites

1. **Python 3.6+** (usually pre-installed on macOS/Linux)
2. **Ollama** - Download from [https://ollama.ai/](https://ollama.ai/)
3. **A language model** - After installing Ollama, pull a model:
   ```bash
   ollama pull llama3.2
   ```

## Installation

### Quick Install
```bash
# Clone or download this repository
git clone <your-repo-url>
cd helper_unix_tool

# Run the installer
chmod +x install.sh
./install.sh
```

### Manual Install
```bash
# Make the script executable
chmod +x help_tool.py

# Create a symlink (requires sudo)
sudo ln -sf /path/to/help_tool.py /usr/local/bin/help
```

## Usage

### Basic Usage
```bash
help "your question or what you want to do"
```

### Examples
```bash
# Find files
help "how to find all text files in current directory"

# System information
help "how to check disk space and memory usage"

# Process management
help "how to find and kill a process"

# File operations
help "how to copy files from one directory to another"

# Network
help "how to check if a port is open"

# Package management (Ubuntu/Debian)
help "how to install a package on Ubuntu"
```

### Advanced Usage
```bash
# Use a different Ollama model
help --model codellama "how to write a bash script"

# Check version
help --version
```

## How it works

1. You type `help "your question"`
2. The tool sends your question to Ollama (local AI)
3. Ollama understands what you want to do
4. You get back the exact command + explanation

## Example Output

```bash
$ help "how to find all PDF files"

🤖 Asking Ollama (llama3.2) for help with: how to find all PDF files
--------------------------------------------------
COMMAND: find . -name "*.pdf"
EXPLANATION: This command searches for all PDF files in the current directory and subdirectories
USAGE: 
- find . -name "*.pdf" (current directory and subdirectories)
- find /path/to/search -name "*.pdf" (specific directory)
- find . -name "*.pdf" -type f (only files, not directories)
```

## Troubleshooting

### "Ollama is not installed"
- Download and install Ollama from [https://ollama.ai/](https://ollama.ai/)
- Make sure it's running: `ollama serve`

### "Model not found"
- Pull the model: `ollama pull llama3.2`
- Or use a different model: `help --model codellama "your question"`

### "Permission denied"
- Make sure the script is executable: `chmod +x help_tool.py`
- Or reinstall: `./install.sh`

### "Command not found"
- Make sure the symlink was created: `ls -la /usr/local/bin/help`
- Reinstall if needed: `./install.sh`

## Customization

### Using Different Models
You can use any Ollama model:
```bash
help --model codellama "your question"
help --model llama3.2 "your question"
help --model mistral "your question"
```

### Installing Models
```bash
# Install different models
ollama pull codellama
ollama pull llama3.2
ollama pull mistral
```

## Contributing

Feel free to improve the tool! Some ideas:
- Add more specific prompts for different types of commands
- Support for different operating systems
- Add command history
- Add interactive mode

## License

MIT License - feel free to use and modify!

---

**Happy coding! 🎉** 