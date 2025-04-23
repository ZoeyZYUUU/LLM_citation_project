# LLM Citation Evaluation Project

This project explores, implements, and compares multiple approaches to generating reliable and traceable citations in outputs produced by large language models (LLMs). The primary goal is to reduce hallucination and improve factual grounding, particularly in high-stakes domains such as healthcare, scientific research, and business intelligence.

## Objectives

- Conduct a literature review of LLM citation methods.
- Implement selected citation strategies such as:
  - Retrieval-Augmented Generation (RAG)
  - Prompt-based inline citation
  - Document and table-aware citation pipelines
- Evaluate performance across multiple modalities (text, structured data).
- Compare API-accessible models including OpenAI, Cohere, and Gemini.
- Apply evaluations on benchmark datasets such as ALCE and LongCite.

## Repository Structure

```bash
LLM_citation_project/
├── ALCE/                        # Dataset: Academic Language Citation Examples
├── models/                     # Custom model wrappers (e.g., GeminiLLM, CohereLLM)
├── test_rag_demo.py            # Main script for baseline RAG experiments
├── requirements.txt            # Project dependencies
├── .gitignore                  # Ignore rules for sensitive files
├── .env                        # Local environment variables (excluded from version control)
└── README.md                   # Project overview and instructions
```

## Experimental Setup

| Experiment Type               | Model             | Dataset     | Objective                                                  |
|------------------------------|-------------------|-------------|-------------------------------------------------------------|
| RAG baseline                 | Cohere / OpenAI   | ALCE        | Evaluate grounding and hallucination behavior              |
| Prompt-based inline citation | Gemini / Claude   | LongCite    | Assess whether inline citations align with sources         |
| Table-based citation         | OpenAI + Tool     | Custom CSV  | Test citation of specific table cells and rows             |

## Setup Instructions

### Clone the repository

```bash
git clone https://github.com/ZoeyZYUUU/LLM_citation_project.git
cd LLM_citation_project

```
### Set up a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configure environment variables:
Create a .env file in the project root with the API keys

## Evaluation Criteria
- Citation granularity (sentence-level, paragraph-level, cell-level)

- Hallucination rate and factual accuracy

- Model response latency and throughput

- Cost-effectiveness and scalability

- Complexity of reference sources and formats

## Next Steps

- Begin implementation of baseline citation experiments

- Extend to more complex retrieval and citation mechanisms

- Prepare evaluation reports and visualizations

- Submit internal milestone report or academic paper draft




