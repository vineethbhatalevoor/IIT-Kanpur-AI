from boltiotai import openai
import os
import sys

while True:
    question = input("Q: What is your question/instruction? \n")

    try:
        openai.api_key = os.environ['OPENAI_API_KEY']
        if openai.api_key == "":
            sys.stderr.write("""
    You haven't set up your API key yet.

    If you don't have an API key yet, visit:

    https://platform.openai.com/signup

    1. Make an account or sign in
    2. Click "View API Keys" from the top right menu.
    3. Click "Create new secret key"

    Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
    """)
            exit(1)

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )

        output = response["choices"][0]["message"]["content"]
        print("Answer:",output, "\n")

    except KeyError:
        print("Environment variable OPENAI_API_KEY not set.")
    except Exception as e:
        print(f"An error occurred: {e}")

