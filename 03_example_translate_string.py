from helper import get_chat_completion

# 1. asking chatGPT to translate a english sentense to other language without formatting

text = f"""
virtual private network (VPN)
"""

prompt = f"""
translate the text in triple backticks \ 
into other languages including Spinish, German, Portuguese, Russian.
```{text}```
"""

response = get_chat_completion(prompt)
print(response)

"""
Output:
Spanish: red privada virtual (VPN)
German: virtuelles privates Netzwerk (VPN)
Portuguese: rede privada virtual (VPN)
Russian: виртуальная частная сеть (VPN)
"""




# 2. asking chatGPT to translate with simple listing

text_2 = f"""
virtual-private-network: virtual private network (VPN)
"""
prompt = f"""

translate the text written in english which delimited by triple quotes \
into other languages including French, Spinish, German, Portuguese, Romanian and Italian.
please present the language code belongs to the language and format the output like:

en:
virtual-private-network: virtual private network (VPN)


please include the english one in the result.
\"\"\"{text_2}\"\"\"
"""
response = get_completion(prompt)
print("Completion for Text 2:")
print(response)

"""
output:

Completion for Text 2:
en:
virtual-private-network: virtual private network (VPN)

fr:
virtual-private-network: réseau privé virtuel (VPN)

es:
virtual-private-network: red privada virtual (VPN)

de:
virtual-private-network: virtuelles privates Netzwerk (VPN)

pt:
virtual-private-network: rede privada virtual (VPN)

ro:
virtual-private-network: rețea privată virtuală (VPN)

it:
virtual-private-network: rete privata virtuale (VPN)

"""




# 3. asking chatGPT to translate with simple listing and order the result

text_2 = f"""
virtual-private-network: virtual private network (VPN)
"""
prompt = f"""

translate the text written in english which delimited by triple quotes \
into other languages including French, Spinish, German, Portuguese, Romanian and Italian.
please present the language code belongs to the language and format the output as JSOM format like:

{
    "key": "virtual-private-network",
    "display": "virtual private network (VPN)"
}


please include the english one in the result.
\"\"\"{text_2}\"\"\"
"""
response = get_completion(prompt)
print("Completion for Text 2:")
print(response)


# 4. asking chatGPT to translate with simple listing and return as JSON

text_2 = f"""
virtual-private-network: virtual private network (VPN)
"""
prompt = f"""
translate the text written in english which delimited by triple quotes \
into other languages including French, Spinish, German, Portuguese, \
Romanian and Italian.
please present the language code belongs to the language and format \
the output as a JSON list with the keys "key", "code" and "display".
please include the english one in the result.

\"\"\"{text_2}\"\"\"
"""

response = get_completion(prompt)
print("Completion for Text 2:")
print(response)


"""
output:

Completion for Text 2:
[
  {
    "key": "virtual-private-network",
    "code": "en",
    "display": "virtual private network (VPN)"
  },
  {
    "key": "réseau-privé-virtuel",
    "code": "fr",
    "display": "réseau privé virtuel (VPN)"
  },
  {
    "key": "red-privada-virtual",
    "code": "es",
    "display": "red privada virtual (VPN)"
  },
  {
    "key": "virtuelles-privates-netzwerk",
    "code": "de",
    "display": "virtuelles privates Netzwerk (VPN)"
  },
  {
    "key": "rede-privada-virtual",
    "code": "pt",
    "display": "rede privada virtual (VPN)"
  },
  {
    "key": "rețea-privată-virtuală",
    "code": "ro",
    "display": "rețea privată virtuală (VPN)"
  },
  {
    "key": "rete-privata-virtuale",
    "code": "it",
    "display": "rete privata virtuale (VPN)"
  }
]
"""


# 5. use <> in indicate the format we want:

text_2 = f"""
virtual-private-network: virtual private network (VPN)
ssl: SSL, or Secure Sockets Layer
"""

prompt = f"""
translate the text written in english which delimited by triple quotes \
into other languages including French, Spinish, German, Portuguese, Romanian and Italian.
please present the language code belongs to the language and format like:

<language code>:
<key>: <translated result>


please include the english one in the result.
\"\"\"{text_2}\"\"\"
"""
response = get_completion(prompt)
print("Completion for Text 2:")
print(response)



"""
output:

Completion for Text 2:
fr:
virtual-private-network: réseau privé virtuel (VPN)
ssl: SSL, ou Secure Sockets Layer

es:
virtual-private-network: red privada virtual (VPN)
ssl: SSL, o Capa de Sockets Seguros

de:
virtual-private-network: virtuelles privates Netzwerk (VPN)
ssl: SSL oder Secure Sockets Layer

pt:
virtual-private-network: rede privada virtual (VPN)
ssl: SSL ou Camada de Sockets Seguros

ro:
virtual-private-network: rețea privată virtuală (VPN)
ssl: SSL sau Secure Sockets Layer

it:
virtual-private-network: rete privata virtuale (VPN)
ssl: SSL o Secure Sockets Layer
"""
