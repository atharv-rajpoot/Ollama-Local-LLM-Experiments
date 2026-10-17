# Ollama Local LLM Experiments

A collection of Python experiments exploring local large language models (LLMs), text generation, LangChain integration, and text embeddings using Ollama.

This project demonstrates how to download and run open-source models locally, interact with them through Python, and generate numerical representations of text for downstream machine learning applications.

## Project Structure

| File | Description |
|---|---|
| `ollama_qwen_chat.py` | Text generation using Qwen 2.5 3B |
| `ollama_chat_example.py` | Direct interaction with Llama 3.2 using Python |
| `langchain_ollama_chat.py` | Llama 3.2 integration with LangChain |
| `ollama_embeddings_example.py` | Text embeddings using Nomic Embed Text |
| `requirements.txt` | Python dependencies |

## Prerequisites

- Python 3.10 or newer recommended
- Ollama
- Git (optional, for cloning the repository)
- Sufficient memory and storage for local models

## 1. Install Ollama

Download Ollama from the official website:

https://ollama.com/download

Verify the installation:

```bash
ollama --version
```

## 2. Download the Models

Run these commands in your terminal:

```bash
ollama pull qwen2.5:3b
ollama pull llama3.2
ollama pull nomic-embed-text
```

Check the downloaded models:

```bash
ollama list
```

## 3. Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/ollama-local-llm-experiments.git
cd ollama-local-llm-experiments
```

Alternatively, download the repository ZIP from GitHub and extract it.

## 4. Create a Python Virtual Environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If using Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Upgrade pip and install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 5. Install Dependencies Manually

If you prefer to install the packages individually:

```bash
python -m pip install ollama
python -m pip install langchain-ollama
```

## 6. Run the Experiments

Ensure Ollama is running and the required model has been downloaded.

### Qwen 2.5 3B

```bash
python ollama_qwen_chat.py
```

Explores text generation and questions about machine learning using Qwen 2.5 3B.

### Llama 3.2 with Python

```bash
python ollama_chat_example.py
```

Sends a prompt to Llama 3.2 using the Ollama Python package.

### Llama 3.2 with LangChain

```bash
python langchain_ollama_chat.py
```

Uses LangChain's `ChatOllama` integration to generate a response.

### Text Embeddings with Nomic

```bash
python ollama_embeddings_example.py
```

Generates embeddings for text and documents using `nomic-embed-text`.

## 7. Useful Ollama Commands

Run a model interactively:

```bash
ollama run llama3.2
```

List available local models:

```bash
ollama list
```

Check currently running models:

```bash
ollama ps
```

Download a model:

```bash
ollama pull MODEL_NAME
```

## Troubleshooting

**Connection refused:** Ensure the Ollama application or service is running.

**Model not found:** Download the required model using `ollama pull`.

**Module not found:** Activate the virtual environment and install the dependencies.

**Slow inference:** Performance depends on available RAM, processor, GPU support, and model size.

## Key Concepts Explored

- Local inference with open-source LLMs
- Python-based text generation
- LangChain integration with Ollama
- Text and document embeddings
- Python virtual environments and dependency management

## Notes

- Models are downloaded separately and are not stored in this repository.
- An internet connection is required for initial model and package downloads.
- Model responses and inference times may vary depending on hardware and model configuration.
