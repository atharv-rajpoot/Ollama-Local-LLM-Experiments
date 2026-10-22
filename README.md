# Ollama Local LLM Experiments

A collection of Python experiments exploring local Large Language Models (LLMs) using Ollama. This project demonstrates text generation, interaction with locally hosted models, LangChain integration, and text embeddings.

The project uses Qwen 2.5 3B, Llama 3.2, and Nomic Embed Text to explore different capabilities of locally running AI models.

## Project Structure

| File | Description |
|---|---|
| `ollama_qwen_chat.py` | Text generation and exploration of machine learning concepts using Qwen 2.5 3B |
| `ollama_chat_example.py` | Direct interaction with Llama 3.2 using the Ollama Python library |
| `langchain_ollama_chat.py` | Integration of Llama 3.2 with LangChain |
| `nomic-embed-text Model Testing.py` | Generation of text and document embeddings using Nomic Embed Text |
| `requirements.txt` | Python dependencies required to run the project |

## Prerequisites

Before running the project, ensure you have:

- Python 3.10 or newer recommended
- Ollama installed on your computer
- Visual Studio Code or another Python-compatible IDE
- An internet connection to download models and Python packages
- Sufficient RAM and storage for local model inference

## 1. Install Ollama

Download and install Ollama from the official website:

https://ollama.com/download

After installation, open Command Prompt, PowerShell, or the VS Code terminal and verify the installation:

```bash
ollama --version
```

Ollama runs the language models locally and provides an interface for applications to interact with them.

## 2. Download the Required Models

Download the models used in this project.

### Qwen 2.5 3B

```bash
ollama pull qwen2.5:3b
```

Used for text generation and explaining machine learning concepts.

### Llama 3.2

```bash
ollama pull llama3.2
```

Used for direct Python chat and LangChain integration.

### Nomic Embed Text

```bash
ollama pull nomic-embed-text
```

Used to generate numerical vector representations of text.

To verify that the models have been downloaded, run:

```bash
ollama list
```

Models are downloaded separately and do not need to be downloaded every time you run a script.

## 3. IDE Setup Using Visual Studio Code

1. Download and install [Visual Studio Code](https://code.visualstudio.com/).
2. Install Python from [python.org](https://www.python.org/downloads/) if it is not already installed.
3. Open VS Code and install the **Python extension by Microsoft**.
4. Open the folder containing the project files.
5. Open the integrated terminal using **Terminal → New Terminal**.
6. Verify that Python is available:

   ```bash
   python --version
   ```

7. Open the Command Palette with `Ctrl + Shift + P`, search for **Python: Select Interpreter**, and select your installed Python version.

You can now run the Python scripts directly from the VS Code terminal.

## 4. Install Python Dependencies

This project uses two Python packages:

- **ollama:** Provides a Python interface for interacting with Ollama models.
- **langchain-ollama:** Provides LangChain integrations for Ollama chat models and embeddings.

Install all dependencies from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Alternatively, install the packages individually:

```bash
python -m pip install ollama
python -m pip install langchain-ollama
```

### requirements.txt

The file should contain:

```text
ollama
langchain-ollama
```

## 5. Run the Python Scripts

Before running a script, ensure Ollama is running and the corresponding model has been downloaded.

### A. Qwen 2.5 3B Chat

**File:** `ollama_qwen_chat.py`

Run:

```bash
python ollama_qwen_chat.py
```

This script demonstrates how to interact with Qwen 2.5 3B through Python. The example prompts explore:

- Machine learning fundamentals
- Supervised versus unsupervised learning
- Neural networks explained in simple terms

The model can also be run directly from the terminal:

```bash
ollama run qwen2.5:3b
```

### B. Direct Ollama Chat

**File:** `ollama_chat_example.py`

Run:

```bash
python ollama_chat_example.py
```

This script uses the `ollama` Python package to send a prompt to Llama 3.2 and print the generated response.

It demonstrates basic programmatic interaction with a locally running language model.

### C. LangChain Integration

**File:** `langchain_ollama_chat.py`

Run:

```bash
python langchain_ollama_chat.py
```

This script uses `ChatOllama` from `langchain_ollama` to invoke Llama 3.2 and display the response.

It demonstrates how LangChain can provide a common interface for interacting with locally hosted language models.

### D. Text Embeddings with Nomic

**File:** `nomic-embed-text Model Testing.py`

Run:

```bash
python "nomic-embed-text Model Testing.py"
```

This script uses `OllamaEmbeddings` to generate vector representations of text.

It demonstrates:

- Generating an embedding for a single sentence
- Generating embeddings for multiple documents
- Checking the dimensionality of an embedding vector
- Checking the number of document embeddings returned

Text embeddings can be used in applications such as semantic search, document similarity, and retrieval-augmented generation (RAG).

## 6. Useful Ollama Commands

| Command | Purpose |
|---|---|
| `ollama --version` | Check the installed Ollama version |
| `ollama list` | List downloaded models |
| `ollama ps` | View currently running models |
| `ollama pull qwen2.5:3b` | Download Qwen 2.5 3B |
| `ollama pull llama3.2` | Download Llama 3.2 |
| `ollama pull nomic-embed-text` | Download Nomic Embed Text |
| `ollama run llama3.2` | Start an interactive Llama 3.2 session |

Ollama usually runs as a background service after installation. If it is not running and your installation supports manual startup, execute:

```bash
ollama serve
```

Do not start a second service if Ollama is already running.

## 7. Troubleshooting

### Ollama Connection Error

Ensure that the Ollama application or service is running. Its default local API endpoint is:

```text
http://localhost:11434
```

### Model Not Found

Download the required model using the appropriate `ollama pull` command.

### Python Module Not Found

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Make sure you are using the same Python interpreter in VS Code that you use to install the packages.

### Python Command Not Recognized

Verify that Python is installed and available in your system PATH. Depending on your operating system, you may need to use `python3` instead of `python`.

### Slow Model Responses

Inference performance depends on RAM, CPU, GPU support, and model size. Close unnecessary applications if your system is running low on memory.

## 8. Key Concepts Explored

- Local inference using open-source LLMs
- Python-based interaction with Ollama
- Prompting and text generation
- LangChain integration with local language models
- Text and document embeddings
- Embedding dimensionality and document vectorization
- Python package installation and IDE-based development

## 9. Notes

- Ollama manages model downloads separately from the Python project.
- An internet connection is required for the initial model and package downloads.
- Once models and dependencies are installed, inference can generally run locally without a hosted LLM API.
- Model responses may vary depending on the prompt and model configuration.
- The embedding script requires the `nomic-embed-text` model, while the chat scripts require their respective chat models.
- Model performance depends on the hardware available.

## 10. Essential Ollama Commands

These commands help manage Ollama, download models, run local LLMs, and remove models when they are no longer needed.

| Command | Description |
|---|---|
| `ollama` | Display available commands and help |
| `ollama --version` | Check the installed Ollama version |
| `ollama serve` | Start the Ollama server manually if it is not already running |
| `ollama pull <model>` | Download a model |
| `ollama list` | List downloaded models |
| `ollama run <model>` | Run a model interactively |
| `ollama rm <model>` | Remove a downloaded model |
| `ollama ps` | Display models currently running in memory |
| `ollama show <model>` | Display model information |
| `ollama stop <model>` | Stop a running model |
| `ollama cp <source> <destination>` | Copy a model under a different name |

### Examples

**1. Download a model**
```bash
ollama pull llama3.2
```

**2. List downloaded models**
```bash
ollama list
```

**3. Run a model**
```bash
ollama run llama3.2
```

Type `/bye` to exit the interactive chat session.

**4. Remove a model**
```bash
ollama rm llama3.2
```

**5. Check running models**
```bash
ollama ps
```

**6. View model information**
```bash
ollama show qwen2.5:3b
```

**7. Stop a running model**
```bash
ollama stop llama3.2
```

**8. Start the Ollama server manually**
```bash
ollama serve
```

> **Note:** Replace model names with the appropriate names from `ollama list`. Ollama usually runs automatically in the background after installation, so you only need `ollama serve` if the server is not already running.
