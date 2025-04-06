mulyi_agent_recommender/
│
├── agents/
│   ├── customer_agent.py         # Handles customer profiling and embeddings
│   ├── product_agent.py          # Handles product info and embeddings
│   ├── recommender_agent.py      # Core logic to generate recommendations
│   ├── data_agent.py             # Handles DB queries, updates, and memory
│   └── tool_agents/
│       ├── web_scraper.py        # Tool agent to scrape live product data
│       ├── api_connector.py      # Tool to fetch real-time inventory, pricing
│       └── ml_predictor.py       # Optional ML model for churn or intent
│
├── database/
│   ├── schema.sql                # Schema for SQLite (products, customers, logs)
│   └── db_utils.py               # Utility functions to interact with SQLite
│
├── embeddings/
│   └── embedding_utils.py        # Generate embeddings using Ollama-based models
│
├── llm/
│   └── ollama_interface.py       # Wrapper for querying on-prem LLMs (Ollama)
│
├── configs/
│   └── settings.yaml             # Configs for DB path, model names, etc.
│
├── interface/
│   ├── cli_interface.py          # Simple CLI for testing agents
│   └── api_server.py             # REST API using FastAPI
│
├── tests/
│   └── test_agents.py            # Unit tests for each agent
│
├── main.py                       # Entry point to run the agent pipeline
└── README.md                     # Project documentation

--- README.md ---

# SmartShop AI - Multi-Agent Recommender System

## 🚀 Overview
SmartShop AI is a multi-agent intelligent product recommendation system for e-commerce, powered by Ollama-based local LLMs. It utilizes multiple agents to analyze user behavior and deliver hyper-personalized recommendations.

## 🧠 Tech Stack
- **Ollama** with **Mistral** (local LLM)
- SQLite for memory and storage
- Python Agents (modular)
- Embedding-based product similarity
- Web scraping + APIs for live product info

## 🧩 Agents
- `CustomerAgent`: Profile users + generate embeddings
- `ProductAgent`: Embed and manage product info
- `RecommenderAgent`: Core recommendation logic
- `DataAgent`: Memory, DB ops, logging
- Tools: Web scraper, API connector, ML predictor

## 📦 Folder Structure
See top-level structure listed above ⬆️

## 🛠️ How to Run
1. Install dependencies:
```bash
pip install pandas numpy fastapi uvicorn
```
2. Start Ollama with Mistral:
```bash
ollama run mistral
```
3. Run main pipeline:
```bash
python main.py
```
4. (Optional) Run CLI:
```bash
python interface/cli_interface.py
```
5. (Optional) Run REST API:
```bash
uvicorn interface.api_server:app --reload
```

## 📄 Dataset
- `customer_data_collection.csv`
- `product_recommendation_data.csv`

## ✅ Features
- Customer profiling using LLM embeddings
- Real-time and static product recommendations
- Agents collaborate and persist context
- Extendable via API tools and ML models

## 🔐 Local + Secure
All models run locally. No cloud dependency.

## 📬 Contact
Built for GFG Hackathon. For demo or issues, ping the team!

--- END ---

