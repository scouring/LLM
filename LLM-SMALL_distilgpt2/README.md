# Lightweight GPT2 Chatbot (CPU Friendly)

This project uses the `distilgpt2` model from Hugging Face for lightweight text generation on CPU — no GPU required.

## Setup

1. Create a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\Activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the chatbot

```bash
python app.py
```

Type a message, and the bot will respond. Type `exit` to quit.

## Model

Uses `distilgpt2`, a distilled version of GPT-2. It's around 300MB and works well for basic NLP demos on CPUs.
