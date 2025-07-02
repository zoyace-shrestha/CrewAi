# CrewAI Example Project

This is a simple example project demonstrating how to use CrewAI to create a team of AI agents that work together to accomplish tasks.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install crewai langchain-openai python-dotenv
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the example:
```bash
python main.py
```

This example creates two agents:
1. A Research Analyst who researches AI in healthcare
2. A Content Writer who creates a blog post based on the research

The agents work sequentially to produce the final output.

## Project Structure

```
.
├── .env                # Environment variables (API keys)
├── README.md          # This file
└── main.py            # Main example script
```

## Requirements

- Python 3.10 or higher
- OpenAI API key
- Required packages (see requirements.txt)