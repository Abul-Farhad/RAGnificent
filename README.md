# SimpleRAG - Easy Multi-Tool Chatbot Toolkit

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![RAG](https://img.shields.io/badge/arch-RAG-ff69b4.svg)
![LLM Compatible](https://img.shields.io/badge/LLM-OpenAI_Compatible-blueviolet.svg)

SimpleRAG is a Python package that enables developers to quickly build powerful chatbots with seamless tool integration and Retrieval-Augmented Generation (RAG) capabilities, supporting any OpenAI-compatible LLM.

## Features

- **Multi-LLM Support** - Works with Groq, OpenAI, Gemini, and any OpenAI-compatible API
- **Easy Tool Integration** - Add custom functions as tools with minimal code
- **Flexible Configuration** - Support for both cloud and self-hosted LLMs
- **Conversation Management** - Built-in thread tracking and user context
- **Prompt Customization** - Flexible system and summary prompts
- **Lightweight** - Minimal dependencies, maximum functionality

## Installation

1. Download the package from GitHub
2. Install using pip:

```bash
pip install path/to/simple_rag-<version>-py3-none-any.whl
```

## Quick Start

```python
from simple_rag import SimpleChatAI, AgentParams
import os

def add(x: int, y: int) -> int:
    """Add two numbers together."""
    return x + y

tools = [add]

# For OpenAI-compatible endpoints
rag = SimpleChatAI()
chatbot = rag.initiate_chatbot(
    params=AgentParams(
        model="gpt-3.5-turbo",  # Or any other model
        api_key="your_api_key",
        base_url="https://api.openai.com/v1",   # Or your custom endpoint
        system_prompt="You are a helpful AI assistant.",
        summary_prompt="Summarize the conversation concisely.",
        thread_id='1',
        tools=tools,    # Optional
        temperature=0.7 # Optional
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
| `base_url`        | str            | API base URL (default: OpenAI)              | No       |
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

## Best Practices

1. Use environment variables for API keys
2. Include clear docstrings for your tools
3. Use type hints for better tool understanding
4. Keep system prompts concise but descriptive
5. Handle sensitive user information appropriately
