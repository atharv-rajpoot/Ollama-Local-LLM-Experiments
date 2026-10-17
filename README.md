# Ollama Local LLM Experiments

A beginner-friendly collection of Python experiments using [Ollama](https://ollama.com/) to run open-source language models locally. This project demonstrates command-line interaction, Python-based chat, LangChain integration, and text embeddings.

## Project Overview

| File | Description |
|---|---|
| `ollama_beginner_assignment.py` | Workshop assignment using Qwen 2.5 3B |
| `ollama_chat_example.py` | Direct Python interaction with Llama 3.2 |
| `langchain_ollama_chat.py` | Chat with Llama 3.2 using LangChain |
| `ollama_embeddings_example.py` | Generate text embeddings using Nomic Embed Text |
| `requirements.txt` | Python dependencies |

## Prerequisites

- Windows, Linux, or macOS
- Python 3.10 or newer recommended
- Ollama installed
- Internet connection for downloading models and Python packages
- Sufficient RAM and disk space for the selected models

## 1. Install Ollama

Download and install Ollama from the official website:

https://ollama.com/download

After installation, open Command Prompt or PowerShell and verify the installation:

```bash
ollama --version
```

If the command is not recognized, reopen your terminal or check that Ollama is correctly installed and available in your PATH.

## 2. Download the Models

Run the following commands in your terminal:

```bash
ollama pull qwen2.5:3b
ollama pull llama3.2
ollama pull nomic-embed-text
```

These models serve different purposes:

- **Qwen 2.5 3B:** Beginner workshop assignment and general text generation.
- **Llama 3.2:** Local chat and LangChain integration.
- **Nomic Embed Text:** Converts text into numerical embedding vectors.

You only need to download each model once. The models remain available locally until removed.

To view downloaded models:

```bash
ollama list
```

## 3. Verify Ollama Is Running

Ollama normally runs as a background service after installation.

Check whether its local API is responding:

```bash
ollama ps
```

You can also test a model directly:

```bash
ollama run llama3.2
```

Enter a prompt and press Enter. Use `/bye` to exit the interactive session.

If Ollama is not running, start the Ollama application. On installations where the service is not started automatically, you can run:

```bash
ollama serve
```

If the service is already running, do not start a second instance.

## 4. Clone the Repository

Install Git if necessary:

https://git-scm.com/downloads

Clone your repository, replacing the URL with your actual GitHub repository URL:

```bash
git clone https://github.com/YOUR_USERNAME/ollama-local-llm-experiments.git
cd ollama-local-llm-experiments
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

## 5. Set Up the Python Environment

Check your Python and pip installations:

```bash
python --version
python -m pip --version
```

Create a virtual environment:

### Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Upgrade pip and install the required packages:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

You can also install the packages individually:

```bash
python -m pip install ollama
python -m pip install langchain-ollama
```

## 6. Run the Python Scripts

Make sure Ollama is running and the relevant model has been downloaded before executing a script.

### A. Beginner Workshop Assignment

```bash
python ollama_beginner_assignment.py
```

Uses Qwen 2.5 3B to demonstrate Python-based questions about machine learning and neural networks.

The script also documents the Ollama CLI commands used in the assignment.

### B. Direct Ollama Chat

```bash
python ollama_chat_example.py
```

Uses Llama 3.2 through the `ollama` Python package to answer a question about artificial intelligence.

### C. LangChain Integration

```bash
python langchain_ollama_chat.py
```

Uses `ChatOllama` from `langchain-ollama` to send a prompt to Llama 3.2 and print the response.

### D. Text Embeddings

```bash
python ollama_embeddings_example.py
```

Uses the Nomic Embed Text model to generate an embedding for a sentence and embeddings for a list of documents.

The script prints the embedding vector length and the number of document embeddings generated.

## 7. Verify the Installation

To confirm that the required models are available:

```bash
ollama list
```

To check the Python packages:

```bash
python -m pip show ollama
python -m pip show langchain-ollama
```

To test a model independently of Python:

```bash
ollama run qwen2.5:3b
```

## Troubleshooting

**Connection refused or Ollama connection error**

Ensure the Ollama application or service is running. The default local API endpoint is `http://localhost:11434`.

**Model not found**

Download the required model using the corresponding `ollama pull` command.

**Python module not found**

Activate your virtual environment and install the dependencies again using `python -m pip install -r requirements.txt`.

**PowerShell activation error**

Use Command Prompt activation or follow the official Python documentation for virtual environments.

**Slow responses or insufficient memory**

Local inference performance depends on model size, available RAM, processor, and GPU support. Smaller models may run more comfortably on limited hardware.

## Learning Outcomes

- Running open-source language models locally with Ollama.
- Using the Ollama CLI and Python package.
- Integrating Ollama models with LangChain.
- Generating text embeddings for individual texts and documents.
- Managing Python dependencies and virtual environments.

## Notes

- Model responses may vary between runs.
- The first model download requires an internet connection.
- Once downloaded, models can generally be used locally without sending prompts to a hosted LLM API.
- This repository contains example scripts for learning and experimentation.
