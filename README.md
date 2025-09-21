# Python AI Agent

A simple AI research assistant using Google's Gemini model and LangChain.

**Note**: I'm not an expert, this is just for learning purposes.

## What This Does

This project creates an AI agent that can answer questions and provide structured responses. It uses:
- **Google's Gemini AI** - The "brain" that processes and answers questions
- **LangChain** - A framework that helps build AI applications
- **Pydantic** - Ensures the AI's responses are properly formatted

When you run it, the agent will answer a sample question and return information like:
- A summary of the topic
- Sources it would use
- Tools it utilized

## Setup

1. **Install dependencies** (the required packages):
```bash
pip install -r requirements.txt
```

2. **Configure your `.env` variables** (create a file called `.env` in the project folder):
```
GOOGLE_API_KEY=your_api_key_here
```

You'll need to get a Google API key from [Google AI Studio](https://aistudio.google.com/) to use the Gemini model.

## Usage

Run the main script:
```bash
python main.py
```

This will ask the AI "What is the capital of France?" and show you how the structured response works.

## Files Explained

- `main.py` - The main code that sets up and runs the AI agent
- `tools.py` - Where you can add custom tools for the agent (currently empty)
- `requirements.txt` - List of Python packages needed
- `.env` - Your secret API keys (you create this)

## Next Steps for Learning

- Try changing the question in `main.py`
- Add custom tools in `tools.py`
- Modify the response format in the `ResearchResponse` class
