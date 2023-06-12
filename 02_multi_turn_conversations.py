from helper import get_chat_completion


messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Lists the top 10 companies in the S&P 500"},
]
response = get_chat_completion(messages, temperature=1)
print(response)

"""
output:

Sure, here are the top 10 companies in the S&P 500 index based on market capitalization as of August 31, 2021:

1. Apple Inc.
2. Microsoft Corporation
3. ...
(skip)
"""