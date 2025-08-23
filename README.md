# MINI-RAG-APP

This is the minimal implementation of the RAG model for answering questions.

## Requirements

- Python 3.13.5 or later

#### Install Python Using MiniConda

1) Download and Install MiniConda.
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag-app python=3.13.5
```
3) Activate the environment:
```bash
$ conda activate mini-rag-app
```

## Installation

### Install the required packages

```bash
$ pip install -r requierments.txt
```

### setup the environment variables

```bash
$ cp .env.example .env
```

set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.