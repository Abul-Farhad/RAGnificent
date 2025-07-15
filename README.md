
# SimpleRAG - Easy Multi-Tool Chatbot Framework

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![RAG](https://img.shields.io/badge/arch-RAG-ff69b4.svg)

SimpleRAG is a Python package that enables developers to quickly build powerful chatbots with seamless tool integration and Retrieval-Augmented Generation (RAG) capabilities.

## Features

- **Easy Tool Integration** - Add custom functions as tools with minimal code
- **Multi-Model Support** - Compatible with Groq's high-performance LLMs
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
from simple_rag import SimpleRag, AgentParams

def add(x: int, y: int) -> int:
    """Add two numbers together."""
    return x + y

tools = [add]

chatbot = SimpleRag(
    params=AgentParams(
        groq_model='deepseek-r1-distill-llama-70b',
        groq_api_key="your_api_key_here",
        system_prompt="You are a helpful AI assistant.",
        summary_prompt="Summarize the conversation concisely.",
        thread_id=1,
        user_information={"Name": "User"},
        tools=tools
    )
).initiate_chatbot()

while True:
    user_input = input("You: ")
    if user_input.lower() == 'q':
        break
    response = chatbot.run(messages=user_input)
    print("AI:", response)
```

## Configuration Options

### AgentParams

| Parameter         | Type     | Description                                  | Required |
|-------------------|----------|----------------------------------------------|----------|
| `groq_model`      | str      | Groq model name                              | Yes      |
| `groq_api_key`    | str      | Your Groq API key                            | Yes      |
| `system_prompt`   | str      | Initial system prompt                        | Yes      |
| `summary_prompt`  | str      | Prompt for conversation summaries            | Yes      |
| `thread_id`       | int      | Conversation thread identifier               | Yes      |
| `user_information`| dict     | User metadata for personalization            | No       |
| `tools`          | list[callable] | Custom tools/functions to integrate      | No       |

## Adding Custom Tools

Simply define Python functions with type hints and docstrings, then pass them in the `tools` list:

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

1. Always include clear docstrings for your tools
2. Use type hints for better tool understanding
3. Keep system prompts concise but descriptive
4. Rotate API keys for security
5. Handle sensitive user information appropriately

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT License - See LICENSE file for details.


This version:
1. Has all the same great content but in a more compact format
2. Maintains all the important sections
3. Keeps the code blocks and tables properly formatted
4. Uses simpler emoji formatting for better compatibility
5. Is ready to paste directly into your GitHub README.md file