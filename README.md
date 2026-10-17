# Ollama Local LLM Experiments

A collection of Python experiments exploring local Large Language Models (LLMs) using Ollama. This project demonstrates how to interact with language models, integrate Ollama with LangChain, and generate text embeddings using Nomic Embed Text.

## Project Structure

| File | Description |
|---|---|
| `langchain_ollama_chat.py` | Interact with Llama 3.2 using LangChain |
| `nomic-embed-text Model Testing.py` | Generate text and document embeddings using Nomic Embed Text |
| `ollama_chat_example.py` | Interact with Llama 3.2 using the Ollama Python library |
| `requirements.txt` | Python dependencies required by the project |

## Prerequisites

Before running the project, ensure you have:

- Python 3.10 or newer recommended
- Ollama installed on your computer
- Visual Studio Code (VS Code) or another Python-compatible IDE
- An internet connection to download models and Python packages

## 1. Install Ollama

Download and install Ollama from its official website:

https://ollama.com/download

After installation, open the terminal in VS Code or Command Prompt and verify that Ollama is installed:

```bash
ollama --version
```

## 2. Download the Models

Download the models required for the experiments using the following commands:

### Llama 3.2

```bash
ollama pull llama3.2
```

Used for generating text responses through the Ollama Python library and LangChain.

### Nomic Embed Text

```bash
ollama pull nomic-embed-text
```

Used to convert text into numerical embedding vectors.

To view your downloaded models, run:

```bash
ollama list
```

## 3. IDE Setup Using Visual Studio Code

1. Download and install [Visual Studio Code](https://code.visualstudio.com/).
2. Install Python from [python.org](https://www.python.org/downloads/) if it is not already installed.
3. Open VS Code and install the **Python** extension published by Microsoft.
4. Open the folder containing your project files.
5. Open the integrated terminal using **Terminal → New Terminal**.
6. Verify Python is available:

   ```bash
   python --version
   ```

7. Select your Python interpreter using **Python: Select Interpreter** from the Command Palette.

You can now execute the scripts from the VS Code terminal.

## 4. Install Python Dependencies

The project uses the following Python packages:

- `ollama`: Communicates with locally running Ollama models.
- `langchain-ollama`: Integrates Ollama models with LangChain and provides chat and embedding interfaces.

Install the dependencies using `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Alternatively, install them individually:

```bash
python -m pip install ollama
python -m pip install langchain-ollama
```

## 5. Run the Python Scripts

Ensure Ollama is running and the required models have been downloaded before executing the scripts.

### A. LangChain Chat

**File:** `langchain_ollama_chat.py`

Run:

```bash
python langchain_ollama_chat.py
```

This script uses LangChain's `ChatOllama` integration to send a prompt to Llama 3.2 and print the generated response.

### B. Text Embeddings

**File:** `nomic-embed-text Model Testing.py`

Run:

```bash
python "nomic-embed-text Model Testing.py"
```

This script uses `OllamaEmbeddings` to generate embeddings for a sentence and a list of text documents. It prints the embedding vector length and the number of document embeddings generated.

### C. Direct Ollama Chat

**File:** `ollama_chat_example.py`

Run:

```bash
python ollama_chat_example.py
```

This script uses the Ollama Python library to send a question to Llama 3.2 and display its response.

## 6. Useful Ollama Commands

| Command | Purpose |
|---|---|
| `ollama --version` | Check the installed Ollama version |
| `ollama list` | List downloaded models |
| `ollama pull llama3.2` | Download Llama 3.2 |
| `ollama pull nomic-embed-text` | Download Nomic Embed Text |
| `ollama run llama3.2` | Start an interactive chat session |
| `ollama ps` | View currently running models |

## 7. Troubleshooting

**Ollama connection error**

Ensure the Ollama application or service is running. The default local API endpoint is `http://localhost:11434`.

**Model not found**

Download the required model using the appropriate `ollama pull` command.

**Module not found**

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

**Python command not recognized**

Ensure Python is installed and available in your system PATH. On some systems, you may need to use `python3` instead of `python`.

**Slow model responses**

Inference speed depends on your available RAM, processor, GPU support, and the size of the model.

## 8. Key Concepts

- Running open-source LLMs locally
- Generating text using Ollama
- Integrating language models with LangChain
- Generating text and document embeddings
- Using Python libraries to interact with local AI models

## 9. Notes

- Ollama manages model downloads separately from the Python project.
- An internet connection is required for initial model and package downloads.
- After the models are downloaded, inference can generally run locally without a hosted LLM API.
- Model performance depends on the hardware available.
- This repository is intended for learning, experimentation, and exploring local AI applications.

