from helper import get_chat_completion

delimiter = "##"

system_message =f"""
You will be provided with IT & helpdesk service queries. \
The IT & helpdesk service query will be delimited with \
{delimiter} characters.

Classify each query into a primary category \
and a secondary category. 

Provide your output in json format with the \
keys: main and sub.

Primary categories: Equipment apply, Account Management, or General Inquiry.

Equipment apply secondary categories:
- Apply/change a desktop/laptop
- Earphone
- Mouse and keyboard
- Footrest
- Monitors

Account Management secondary categories:
- Unable to login via LDAP account
- Password reset
- Update personal information
- Access card

General Inquiry secondary categories:
- Feedback
- Speak to a helpdesk
- General troubleshooting
- Software updates

"""

user_message = f"""\
I want to apply one more monitor and also have my ubunut version to be updated"""
messages =  [  
    {'role':'system',  'content': system_message},
    {'role':'user', 'content': f"{delimiter}{user_message}{delimiter}"},
]

response = get_chat_completion(messages)
print(response)

"""
output:

{
  "main": "Equipment apply",
  "sub": [
    "Monitors",
    "Software updates"
  ]
}
"""