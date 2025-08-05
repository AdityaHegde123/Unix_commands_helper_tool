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

def ask_for_clipboard_copy(command):
    if not command:
        return
    print(f"\nCommand: {command}")
    response = input("Copy to clipboard? (y/n): ").lower().strip()
    if response == 'y' or response == 'yes':
        if copy_to_clipboard(command):
            print("Copied to clipboard.")
        else:
            print("Failed to copy.")

def send_to_ollama(prompt, model="llama3.2"):
    try:
        full_prompt = f"""return only a unix command; no explanation or anything; just the command; no formatting ' ' to enclose the command; here is the prompt {prompt}"""
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
        if command:
            ask_for_clipboard_copy(command)
    else:
        print("No response from Ollama.")
        exit()

if __name__ == "__main__":
    main()