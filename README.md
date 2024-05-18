# LLAMA-RAG-Agent

This project shows my journey in exploring LLAMA and RAG. Here, I create a basic agent with a set of tools: a note writer and a PDF reader. The agent can also analyze CSV data about BTC prices over the last 14 years. Data about all cryptocurrencies was taken from [Kaggle](https://www.kaggle.com/datasets/svaningelgem/crypto-currencies-daily-prices?select=BTC.csv).

---
## Tools

- `md_noter`: Makes and saves notes.
- `pdf_reader`: Creates a vector database and provides data from PDFs.

---
### 1. Clone the Repository

Clone this repository to your local machine using:


```bash
git clone https://github.com/rifolio/LLAMA-RAG-Agent.git
```

---
### 2. Set Up Virtual Environment

Navigate to the project directory and set up a virtual environment by running:

```bash
python3 -m venv ai
```
---
### 3. Activate Virtual Environment

Activate the virtual environment using:

```bash
source ai/bin/activate
```
---
### 4. Install Dependencies

Install the project dependencies using pip:

```bash
pip3 install -r requirements.txt
```

The `requirements.txt` file contains the following packages:

```
python-dotenv
pandas
llama-index
llama-index-experimental
pypdf
```
---
### 5. Initialize API KEY from your OPEN AI Account in .env file and Run the Project

```bash
.env:
OPENAI_API_KEY=
```

Once the dependencies are installed, you can run the project using:

```bash
python3 main.py
```