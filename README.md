# 🧠 Research Assistant Agent

This project is an intelligent research assistant powered by [LangChain](https://www.langchain.com/), 
using the Claude 3.5 Sonnet model. It leverages external tools like Wikipedia and Google Search to gather 
and summarize information in response to user queries.

## 📦 Features

- Uses **Claude 3.5 Sonnet** via `langchain-anthropic`
- Integrates **Wikipedia** and **Google Custom Search** as tools
- Parses responses into structured `Pydantic` models
- Supports conversational memory and multi-step tool use