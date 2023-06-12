from helper import get_completion, get_chat_completion

# 1. simple question

response1_by_prompt = get_completion("What is the capital of California?")
print(response1_by_prompt)

response1_by_chat = get_chat_completion([{"role": "user", "content": "What is the capital of California?"}])
print(response1_by_chat)

# compare the differences:

"""
output from response1_by_prompt:
Sacramento.
"""

"""
output from response1_by_chat:
The capital of California is Sacramento.
"""


# 2. grammar correction

response2_by_prompt = get_completion("correct this to satndard English: ```Please help check this bug for me```")
print(response2_by_prompt)

response2_by_chat = get_chat_completion([{"role": "user", "content": "correct this to satndard English: ```Please help check this bug for me```"}])
print(response2_by_chat)

# compare the differences:

"""
output from response2_by_prompt:
Please help me check this bug.
"""

"""
output from response2_by_chat:
Please help me check this bug.
"""



# 3. text to emoji

response3_by_prompt = get_completion("convert the following sentenses into emoji 'the firefighter is so brave', 'I like boba tea', 'sigh'")
print(response3_by_prompt)
print("----")

response3_by_chat = get_chat_completion([{"role": "user", "content": "convert the following sentenses into emoji 'the firefighter is so brave', 'I like boba tea', 'sigh'"}])
print(response3_by_chat)

# compare the differences:

"""


👨‍🚒🙌😍
"""

"""
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


