"""
How to used Traccia with Groq.
"""

import os

from dotenv import load_dotenv
from groq import Groq
from rich import print
from rich.traceback import install
from traccia import init, observe

install()
load_dotenv()

# Init console export
init(enable_console_exporter=True)

# Create Client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@observe()
def call_model(model):
    """Call model to answer the user question."""

    chat_completion = model.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain me the quantum computing in one sentence",
            }
        ],
        model="llama-3.1-8b-instant",
    )
    return chat_completion


if __name__ == "__main__":
    response = call_model(client)
    print(response)
