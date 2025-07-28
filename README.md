# RAGnificentAI - Your Magnificent RAG-Powered Chatbot Toolkit

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![RAG](https://img.shields.io/badge/arch-RAG-ff69b4.svg)
![LLM Compatible](https://img.shields.io/badge/LLM-OpenAI_Compatible-blueviolet.svg)
![CLI Enabled](https://img.shields.io/badge/CLI-Enabled-green.svg)

RAGnificentAI is a Python package that enables developers to quickly build powerful chatbots with seamless tool integration and Retrieval-Augmented Generation (RAG) capabilities, supporting any OpenAI-compatible LLM.

## Why RAGnificentAI?

- **LLM Agnostic** - Works with Groq, OpenAI, Gemini, and any OpenAI-compatible API
- **Easy Tool Integration** - Add custom functions as tools with minimal code
- **Conversation Management** - Efficient short-term memory management with summarization technique
- **Prompt Customization** - Flexible system and summary prompts
- **Lightweight** - Minimal dependencies, maximum functionality

## Installation

1. Install using pip:

```bash
pip install RAGnificentAI
```

## Quick Start

```python
from RAGnificentAI import ChatAI, AgentParams

def add(x: int, y: int) -> int:
    """Add two numbers together."""
    return x + y


tools = [add]

# For OpenAI-compatible endpoints
rag = ChatAI()
chatbot = rag.initiate_chatbot(
    params=AgentParams(
        model="gpt-3.5-turbo",  # Or any other model
        api_key="your_api_key",
        base_url="https://api.openai.com/v1",  # Or your custom endpoint
        system_prompt="You are a helpful AI assistant.",
        summary_prompt="Summarize the conversation concisely.",
        thread_id='1',
        tools=tools,  # Optional
        temperature=0.7  # Optional
    )
)

while True:
    user_input = input("You (q to quit): ")
    if user_input.lower() == 'q':
        break
    response = chatbot.run(messages=user_input)
    print("AI:", response)
```

## Configuration Options

### AgentParams

| Parameter         | Type           | Description                                  | Required |
|-------------------|----------------|----------------------------------------------|----------|
| `model`           | str            | Model name (e.g. "gpt-3.5-turbo")           | Yes      |
| `api_key`         | str            | Your API key                                | Yes      |
| `base_url`        | str            | API base URL (default: OpenAI)              | Yes      |
| `system_prompt`   | str            | Initial system prompt                       | Yes      |
| `summary_prompt`  | str            | Prompt for conversation summaries           | Yes      |
| `thread_id`       | str            | Conversation thread identifier              | Yes      |
| `user_information`| dict           | User metadata for personalization           | No       |
| `tools`          | list[callable] | Custom tools/functions to integrate         | No       |

## Supported LLM Providers

- OpenAI (including Azure OpenAI)
- Groq
- Gemini
- Any OpenAI-compatible API (LocalAI, vLLM, etc.)
- Anthropic Claude (via OpenAI compatibility layer)

## Adding Custom Tools

```python
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

def get_weather(city: str) -> str:
    """Get current weather for a given city."""
    return f"Weather in {city}: Sunny"

tools = [multiply, get_weather]
```

## New CLI Interface
**Example Workflow:**
```bash
# First-time setup
ragnificentai configure

# Start chatting (uses saved config)
ragnificentai chat

# Override specific settings
ragnificentai chat --model gpt-4 --thread-id special-convo
```

### CLI Features

| Command       | Description                          | Options                              |
|---------------|--------------------------------------|--------------------------------------|
| `chat`        | Start interactive chat session       | `--model`, `--api-key`, `--base-url` |
| `configure`   | Save default configuration           | (interactive wizard)                 |
| `version`     | Show package version                 | None                                 |


## Best Practices

1. Use environment variables for API keys
2. Include clear docstrings for your tools
3. Use type hints for better tool understanding
4. Keep system prompts concise but descriptive
5. Handle sensitive user information appropriately


## License

**RAGnificentAI** is licensed under the **RAGnificentAI Custom License**:  

```text
Copyright (c) 2025 [K. M. Abul Farhad-Ibn-Alam]

Permission is hereby granted to any person obtaining a copy of this software
and associated documentation files (the "Software") to use, modify, and distribute
the Software for any purpose, subject to the following conditions:

1. Redistributions must retain this copyright notice.
2. Commercial use requires written permission from the author.
3. The author is not liable for any damages arising from Software use.

All rights not expressly granted are reserved by the author.

Here's the updated README with the new CLI feature prominently featured, while maintaining all existing content:
```
---