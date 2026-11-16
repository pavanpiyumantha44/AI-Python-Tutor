# AI Python Tutor 🤖 ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

This is a practical Python project as part of learning journey in AI Engineering.

I wanted to get some hands-on experience working with an LLM API and understand how a basic AI chatbot actually works behind the scenes. So, I decided to build a simple terminal-based chatbot using Python and the Groq API.

It's a small project, but it helped me understand several important concepts, especially how to communicate with an LLM, manage conversation history, and handle API errors.

## What can it do?

- Chat with an AI assistant directly through the terminal.
- Answer questions related to Python programming.
- Maintain conversation history during a session.
- Handle common API errors such as authentication failures, rate limits, and connection issues.
- Exit the conversation by typing `/bye`.

## Technologies Used

- **Python 3.14**
- **Groq API** – To communicate with the LLM.
- **Groq Python SDK** – For API integration.
- **python-dotenv** – To manage environment variables.
- **uv** – For Python project and dependency management.

## Project Structure

```text
python-ai-chatbot/
├── src/
│   └── python_chatbot/
│       ├── __init__.py
│       ├── main.py
│       ├── chatbot.py
│       └── config.py
├── .env
├── .gitignore
├── pyproject.toml
└── uv.lock
```

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd python-ai-chatbot
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure the API key

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

### 4. Run the application

```bash
uv run python -m python_chatbot.main
```

That's it! You can now start chatting with your AI assistant through the terminal.

## What I Learned

This project gave me an opportunity to put some Python and LLM fundamentals into practice while exploring AI application development.

Some of the things I learned along the way:

- Working with external APIs using the Groq Python SDK.
- Understanding system, user, and assistant message roles.
- Managing conversation history using Python lists and dictionaries.
- Handling API exceptions using `try-except`.
- Organizing Python code into separate modules.
- Managing API keys securely using environment variables.
- Understanding Python imports and application entry points.

---

*Built as part of my practical learning journey in AI Engineering.*
