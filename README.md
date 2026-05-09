# AI Agent

An autonomous AI agent capable of executing code and manipulating files, built as a learning project with guidance from boot.dev.

⚠️ **SECURITY WARNING**: This project executes arbitrary Python code and modifies files. **Do NOT use in production or on important data.** Always maintain backups before running.

## Overview

AI Agent is a Python-based autonomous system that can analyze tasks and execute them using a set of predefined tools. It's designed for educational purposes to understand how LLM-powered agents can interact with their environment.

## Features

The AI Agent can:
- 📁 List and explore files and directories within the working directory
- 📖 Read file contents
- ✏️ Create new files and edit existing files
- ⚙️ Execute Python programs
- 🔧 Help debug and generate code

## Architecture

- **Working Directory**: Currently hardcoded to the `calculator` directory to prevent unintended file modifications
- **Core Tools**: File system operations and Python execution
- **Primary Use Case**: Code debugging and generation assistance

## Getting Started

### Prerequisites
- Python 3.8+
- Required dependencies (see requirements or setup file if present)

### Installation

```bash
git clone https://github.com/ZachBrunker-2000/AI_Agent.git
cd AI_Agent
# Install dependencies here if applicable
```

### Usage

```bash
python main.py
```

## ⚠️ Important Safety Notes

1. **Backup Everything**: Before running the agent, create backups of any important files or projects
2. **Limited Scope**: The working directory is intentionally restricted to prevent catastrophic changes
3. **Unpredictable Behavior**: The agent may make unexpected file modifications
4. **Not Production-Ready**: This is an educational project and should never be deployed in production environments

## Project Structure

```
AI_Agent/
├── README.md
├── calculator/          # Restricted working directory
│   └── README.md
└── [main code files]
```

## Learning Resources

This project was built following the boot.dev curriculum on AI agents and autonomous systems.

## License

[Add your license here]

## Author

[ZachBrunker-2000](https://github.com/ZachBrunker-2000)

---

**Last Updated**: May 2026