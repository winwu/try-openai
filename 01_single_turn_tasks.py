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

def get_completion(prompt, model="gpt-3.5-turbo"):
    try:
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,
        )
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


# 1. simple question

response1 = get_completion("What is the capital of California?")
print(response1)

"""
output:
The capital of California is Sacramento.
"""





# 2. grammar correction

response2 = get_completion("correct this to satndard English: ```Please help check this bug for me```")
print(response2)

"""
output:
Please help me check this bug.
"""






# 3. text to emoji

response3 = get_completion("convert the following sentenses into emoji 'the firefighter is so brave', 'I like boba tea', 'sigh'")
print(response3)

"""
output:
👨‍🚒💪😎 (the firefighter is so brave)
👍😋🍵 (I like boba tea)
😔😞 (sigh)
"""


# 4. query a result and format

response4 = get_completion("please list the top 5 GDP countries and return the result as JSON format with the key 'country' and 'GDP'")
print(response4)

"""
output: (skip the real content)

{
  "data": [
    {
      "country": "",
      "GDP": 
    },
    {
      "country": "",
      "GDP": 
    },
    {
      "country": "",
      "GDP": 
    },
    {
      "country": "",
      "GDP": 
    },
    {
      "country": "",
      "GDP": 
    }
  ]
}
"""

# 5. write a thank you letter

response5 = get_completion("one of my friend help me a \
lot during my college life, that's assuming her name \
is 'Amber', please write a thank you letter to appreciate \
her company and hope she will have a good future")
print(response5)
print(len(response5))

# in this example, the gpt return 1223 words for me, let's reduce the content
 
"""
output: (skip the real content)
"""


# 5-1. write a thank you letter and restrict the characters in 50, but it actually returns 105 characters

response6 = get_completion("one of my friend help me a \
lot during my college life, that's assuming her name \
is 'Amber', please write a thank you letter to appreciate \
her company and hope she will have a good future, please write a letter in 50 characters")
print(response6)
print(len(response6))
 
"""
output:

Dear Amber, thank you for being there for me in college. Wishing you a bright future ahead. - [Your Name]
105
"""

