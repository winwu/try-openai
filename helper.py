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

def get_completion(prompt, model="text-davinci-003"):
    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
        )

        # complete response format example:
        """
        {
            "choices": [
                {
                "finish_reason": "length",
                "index": 0,
                "logprobs": null,
                "text": "\n\nIt is 10:56pm (EST) on Tuesday, May 19"
                }
            ],
            "created": 1686531859,
            "id": "cmpl-7QQGh2OABsLh1Ym33BL4RUhOCEwEd",
            "model": "text-davinci-003",
            "object": "text_completion",
            "usage": {
                "completion_tokens": 16,
                "prompt_tokens": 5,
                "total_tokens": 21
            }
        }
        """
        return response.choices[0].text

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


def get_chat_completion(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500):
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
