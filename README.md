# 🧠 LLM CPU Flask API

A lightweight local API for running a pre-trained large language model (LLM) on a Windows machine **without a GPU** using **Flask**, **Hugging Face Transformers**, and **PyTorch**.

This project shows how to deploy a pre-trained model like `mistralai/Mistral-7B-Instruct-v0.1` in a resource-constrained environment — ideal for prototyping or learning.

---

## 🚀 Features

- Runs on **CPU** (no GPU required)
- Flask REST API for easy integration
- Uses Hugging Face `transformers` + `pipeline`
- Clean project structure
- Good starting point for local GenAI apps

---

## 🛠️ Tech Stack

- Python 3.8+
- Flask
- Hugging Face Transformers
- PyTorch (CPU)
- Mistral-7B-Instruct or similar open LLM

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/llm-cpu-flask-api.git
cd llm-cpu-flask-api
