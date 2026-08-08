# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.8 or later

### Installing Python Using Miniconda

1) Download and install Miniconda from [Here](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
2) Create the environment using the following commands
``` bash
$ conda create -n mini-rag-app python=3.8
```
3) Activate the environment:
``` bash
$ conda activate mini-rag-app
``` 

# Installation

### Install the required packages

```bash
$ pip install -r requirements.txt 
```

### Setup the environment variable

```bash
$ cp .env.example .env
```

Set your envrionment variables in the `.env` file. Like `OPENAI_API_KEY` value.

### Run the FastAPI server 

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

### POSTMAN Collection 

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)

