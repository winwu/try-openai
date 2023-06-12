import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key = os.environ['OPENAI_API_KEY']

# print(os.environ['OPENAI_API_KEY'])

# helper function
# use gpt-3.5-turbo
# please see https://platform.openai.com/docs/models

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            # Lower values for temperature result in more consistent outputs, while higher values generate more diverse and creative result
            temperature=temperature,
            max_tokens=max_tokens,
        )

        # complete response format example:
        """
        {
            "id": "",
            "object": "chat.completion",
            "created": ,
            "model": "",
            "usage": {
                "prompt_tokens": ,
                "completion_tokens": ,
                "total_tokens":
            },
            "choices": [
                {
                "message": {
                    "role": "assistant",
                    "content": "Here are the top 10 companies in the S&P 500, ..."
                },
                "finish_reason": "stop",
                "index": 0
                }
            ]
        }
        """
        return response.choices[0].message["content"]

    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass

    except openai.error.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass

    except openai.error.RateLimitError as e:
        # Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Lists the top 10 companies in the S&P 500"},
]
response = get_completion_from_messages(messages, temperature=1)
print(response)

"""
output:

Sure, here are the top 10 companies in the S&P 500 index based on market capitalization as of August 31, 2021:

1. Apple Inc.
2. Microsoft Corporation
3. ...
(skip)
"""