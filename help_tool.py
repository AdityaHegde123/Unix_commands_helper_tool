#!/usr/bin/env python3
import os
import subprocess
import argparse
import pyperclip

def copy_to_clipboard(command):
    try:
        pyperclip.copy(command)
        return True
    except Exception as e:
        return False

def send_to_ollama(prompt, model="llama3.2"):
    try:
        full_prompt = f"""return only unix command; no explanation or formatting; ' ' to enclose the command; prompt: {prompt}"""
        result = subprocess.run(["ollama", "run", model, full_prompt], capture_output=True, text=True,timeout=30)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return None
    except Exception:
        return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt")
    parser.add_argument("--model", default="llama3.2")
    args = parser.parse_args()
    command = send_to_ollama(args.prompt, args.model)
    if command:
        print(command)
        if copy_to_clipboard(command):
            print("Copied to clipboard.")
        else:
            print("Failed to copy.")
    else:
        print("No response from Ollama.")
        exit()

if __name__ == "__main__":
    main()